'''

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

'''

def associate_vpc_with_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    Associates an Amazon VPC with a private hosted zone.
    Send a POST request to the /2013-04-01/hostedzone/*hosted zone ID* /associatevpc resource. The request body must include an XML document with a AssociateVPCWithHostedZoneRequest element. The response returns the AssociateVPCWithHostedZoneResponse element.
    
    
    :example: response = client.associate_vpc_with_hosted_zone(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
            'VPCId': 'string'
        },
        Comment='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone you want to associate your VPC with.
            Note that you cannot associate a VPC with a hosted zone that doesn't have an existing VPC association.
            

    :type VPC: dict
    :param VPC: [REQUIRED]
            A complex type containing information about the Amazon VPC that you're associating with the specified hosted zone.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            

    :type Comment: string
    :param Comment: Optional: A comment about the association request.

    :rtype: dict
    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def change_resource_record_sets(HostedZoneId=None, ChangeBatch=None):
    """
    Create, change, update, or delete authoritative DNS information on all Amazon Route 53 servers. Send a POST request to:
    The request body must include a document with a ChangeResourceRecordSetsRequest element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. When using the Amazon Route 53 API to change resource record sets, Amazon Route 53 either makes all or none of the changes in a change batch request. This ensures that Amazon Route 53 never partially implements the intended changes to the resource record sets in a hosted zone.
    For example, a change batch request that deletes the CNAME record for www.example.com and creates an alias resource record set for www.example.com. Amazon Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If either the DELETE or the CREATE action fails, then both changes (plus any other changes in the batch) fail, and the original CNAME record continues to exist.
    Use ChangeResourceRecordsSetsRequest to perform the following actions:
    In response to a ChangeResourceRecordSets request, the DNS data is changed on all Amazon Route 53 DNS servers. Initially, the status of a change is PENDING , meaning the change has not yet propagated to all the authoritative Amazon Route 53 DNS servers. When the change is propagated to all hosts, the change returns a status of INSYNC .
    After sending a change request, confirm your change has propagated to all Amazon Route 53 DNS servers. Changes generally propagate to all Amazon Route 53 name servers in a few minutes. In rare circumstances, propagation can take up to 30 minutes. For more information, see  GetChange .
    For information about the limits on a ChangeResourceRecordSets request, see Limits in the Amazon Route 53 Developer Guide .
    
    
    :example: response = client.change_resource_record_sets(
        HostedZoneId='string',
        ChangeBatch={
            'Comment': 'string',
            'Changes': [
                {
                    'Action': 'CREATE'|'DELETE'|'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'string',
                        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                        'SetIdentifier': 'string',
                        'Weight': 123,
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                        'GeoLocation': {
                            'ContinentCode': 'string',
                            'CountryCode': 'string',
                            'SubdivisionCode': 'string'
                        },
                        'Failover': 'PRIMARY'|'SECONDARY',
                        'TTL': 123,
                        'ResourceRecords': [
                            {
                                'Value': 'string'
                            },
                        ],
                        'AliasTarget': {
                            'HostedZoneId': 'string',
                            'DNSName': 'string',
                            'EvaluateTargetHealth': True|False
                        },
                        'HealthCheckId': 'string',
                        'TrafficPolicyInstanceId': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to change.
            

    :type ChangeBatch: dict
    :param ChangeBatch: [REQUIRED]
            A complex type that contains an optional comment and the Changes element.
            Comment (string) --
            Optional: Any comments you want to include about a change batch request.
            Changes (list) -- [REQUIRED]Information about the changes to make to the record sets.
            (dict) --The information for each resource record set that you want to change.
            Action (string) -- [REQUIRED]The action to perform:
            CREATE : Creates a resource record set that has the specified values.
            DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
            Warning
            To delete the resource record set that is associated with a traffic policy instance, use `` DeleteTrafficPolicyInstance `` . Amazon Route 53will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.
            UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
            ResourceRecordSet (dict) -- [REQUIRED]Information about the resource record set to create or delete.
            Name (string) -- [REQUIRED]The name of the domain you want to perform the action on.
            Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
            You can use the asterisk (*) wildcard to replace the leftmost label in a domain name. For example, *.example.com . Note the following:
            The * must replace the entire label. For example, you can't specify *prod.example.com or prod*.example.com .
            The * can't replace any of the middle labels, for example, marketing.*.example.com.
            If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
            Warning
            You can't use the * wildcard for resource records sets that have a type of NS.
            You can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You cannot use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can't specify prod*.example.com .
            Type (string) -- [REQUIRED]The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            Valid values for basic resource record sets: A | AAAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
            Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
            Note
            SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, '...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.' In RFC 7208, see section 14.1, The SPF DNS Record Type .
            Values for alias resource record sets:
            CloudFront distributions: A
            Elastic Beanstalk environment that has a regionalized subdomain : A
            ELB load balancers: A | AAAA
            Amazon S3 buckets: A
            Another resource record set in this hosted zone: Specify the type of the resource record set for which you're creating the alias. Specify any value except NS or SOA .
            SetIdentifier (string) --
            Weighted, Latency, Geo, and Failover resource record sets only: An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of SetIdentifier must be unique for each resource record set that has the same combination of DNS name and type. Omit SetIdentifier for any other types of record sets.
            Weight (integer) --
            Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:
            You must specify a value for the Weight element for every weighted resource record set.
            You can only specify one ResourceRecord per weighted resource record set.
            You cannot create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
            You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
            For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .
            Region (string) --
            Latency-based resource record sets only: The Amazon EC2 region where the resource that is specified in this resource record set resides. The resource typically is an AWS resource, such as an Amazon EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
            Note
            Creating latency and latency alias resource record sets in private hosted zones is not supported.
            When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 region. Amazon Route 53 then returns the value that is associated with the selected resource record set.
            Note the following:
            You can only specify one ResourceRecord per latency resource record set.
            You can only create one latency resource record set for each Amazon EC2 region.
            You are not required to create latency resource record sets for all Amazon EC2 regions. Amazon Route 53 will choose the region with the best latency from among the regions for which you create latency resource record sets.
            You cannot create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.
            GeoLocation (dict) --
            Geo location resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .
            Note
            Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.
            If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
            You cannot create two geolocation resource record sets that specify the same geographic location.
            The value * in the CountryCode element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the Name and Type elements.
            Warning
            Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of CountryCode is * , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a * resource record set, Amazon Route 53 returns a 'no answer' response for queries from those locations.
            You cannot create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.
            ContinentCode (string) --The two-letter code for the continent.
            Valid values: AF | AN | AS | EU | OC | NA | SA
            Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
            CountryCode (string) --The two-letter code for the country.
            SubdivisionCode (string) --The code for the subdivision, for example, a state in the United States or a province in Canada.
            Failover (string) --
            Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
            Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:
            When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
            When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
            When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
            If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.
            You cannot create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
            For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
            For more information about configuring failover for Amazon Route 53, see the following topics in the Amazon Route 53 Developer Guide :
            Amazon Route 53 Health Checks and DNS Failover
            Configuring Failover in a Private Hosted Zone
            Valid values: PRIMARY | SECONDARY
            TTL (integer) --The resource record cache time to live (TTL), in seconds. Note the following:
            If you're creating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
            If you're associating this resource record set with a health check (if you're adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
            All of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets must have the same value for TTL .
            If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .
            ResourceRecords (list) --Information about the resource records to act upon.
            Note
            If you are creating an alias resource record set, omit ResourceRecords .
            (dict) --Information specific to the resource record.
            Note
            If you are creating an alias resource record set, omit ResourceRecord .
            Value (string) -- [REQUIRED]The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            You can specify more than one value for all record types except CNAME and SOA .
            Note
            If you are creating an alias resource record set, omit Value .
            
            AliasTarget (dict) --
            Alias resource record sets only: Information about the CloudFront distribution, Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you are redirecting queries. The Elastic Beanstalk environment must have a regionalized subdomain.
            If you're creating resource records sets for a private hosted zone, note the following:
            You can't create alias resource record sets for CloudFront distributions in a private hosted zone.
            Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.
            For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .
            HostedZoneId (string) -- [REQUIRED]
            Alias resource records sets only : The value used depends on where the queries are routed:
            A CloudFront distribution
            Specify Z2FDTNDATAQYW2 .
            Note
            Alias resource record sets for CloudFront cannot be created in a private zone.
            Elastic Beanstalk environment
            Specify the hosted zone ID for the region in which you created the environment. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see AWS Elastic Beanstalk in the Regions and Endpoints chapter of the AWS General Reference .
            ELB load balancer
            Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
            AWS Management Console: Go to the Amazon EC2; page, click Load Balancers in the navigation pane, select the load balancer, and get the value of the Hosted Zone ID field on the Description tab. Use the same process to get the DNS Name. See HostedZone$Name .
            Elastic Load Balancing API: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneNameID . Use the same process to get the CanonicalHostedZoneName . See HostedZone$Name .
            AWS CLI: Use `` describe-load-balancers `` to get the value of CanonicalHostedZoneNameID . Use the same process to get the CanonicalHostedZoneName . See HostedZone$Name .An Amazon S3 bucket configured as a static website
            Specify the hosted zone ID for the Amazon S3 website endpoint in which you created the bucket. For more information about valid values, see the table Amazon S3 (S3) Website Endpoints in the Amazon Web Services General Reference .
            Another Amazon Route 53 resource record set in your hosted zone
            Specify the hosted zone ID of your hosted zone. (An alias resource record set cannot reference a resource record set in a different hosted zone.)
            DNSName (string) -- [REQUIRED]
            Alias resource record sets only: The value that you specify depends on where you want to route queries:
            A CloudFront distribution: Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
            Elastic Beanstalk environment : Specify the CNAME attribute for the environment. (The environment must have a regionalized domain name.) You can use the following methods to get the value of the CNAME attribute:
            AWS Managment Console : For information about how to get the value by using the console, see Using Custom Domains with Elastic Beanstalk in the AWS Elastic Beanstalk Developer Guide .
            Elastic Load Balancing API : Use the DescribeEnvironments action to get the value of the CNAME attribute. For more information, see DescribeEnvironments in the AWS Elastic Beanstalk API Reference .
            AWS CLI : Use the describe-environments command to get the value of the CNAME attribute. For more information, see describe-environments in the AWS Command Line Interface Reference .
            An ELB load balancer: Specify the DNS name associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
            AWS Management Console : Go to the Amazon EC2 page, click Load Balancers in the navigation pane, choose the load balancer, choose the Description tab, and get the value of the DNS Name field that begins with dualstack. Use the same process to get the Hosted Zone ID. See HostedZone$Id .
            Elastic Load Balancing API : Use `` DescribeLoadBalancers `` to get the value of CanonicalHostedZoneName . Use the same process to get the CanonicalHostedZoneNameId . See HostedZone$Id .
            AWS CLI : Use `` describe-load-balancers `` to get the value of CanonicalHostedZoneName . Use the same process to get the CanonicalHostedZoneNameId . See HostedZoneId.
            An Amazon S3 bucket that is configured as a static website: Specify the domain name of the Amazon S3 website endpoint in which you created the bucket; for example, s3-website-us-east-1.amazonaws.com . For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference . For more information about using Amazon S3 buckets for websites, see Hosting a Static Website on Amazon S3 in the Amazon Simple Storage Service Developer Guide.
            Another Amazon Route 53 resource record set : Specify the value of the Name element for a resource record set in the current hosted zone.
            EvaluateTargetHealth (boolean) -- [REQUIRED]
            Applies only to alias, weighted alias, latency alias, and failover alias record sets: If you set the value of EvaluateTargetHealth to true for the resource record set or sets in an alias, weighted alias, latency alias, or failover alias resource record set, and if you specify a value for `` HealthCheck$Id `` for every resource record set that is referenced by these alias resource record sets, the alias resource record sets inherit the health of the referenced resource record sets.
            In this configuration, when Amazon Route 53 receives a DNS query for an alias resource record set:
            Amazon Route 53 looks at the resource record sets that are referenced by the alias resource record sets to determine which health checks they're using.
            Amazon Route 53 checks the current status of each health check. (Amazon Route 53 periodically checks the health of the endpoint that is specified in a health check; it doesn't perform the health check when the DNS query arrives.)
            Based on the status of the health checks, Amazon Route 53 determines which resource record sets are healthy. Unhealthy resource record sets are immediately removed from consideration. In addition, if all of the resource record sets that are referenced by an alias resource record set are unhealthy, that alias resource record set also is immediately removed from consideration.
            Based on the configuration of the alias resource record sets (weighted alias or latency alias, for example) and the configuration of the resource record sets that they reference, Amazon Route 53 chooses a resource record set from the healthy resource record sets, and responds to the query.
            Note the following:
            You cannot set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.
            If the AWS resource that you specify in AliasTarget is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target.For more information, see What Happens When You Omit Health Checks? in the Amazon Route 53 Developer Guide .
            If you specify an Elastic Beanstalk environment in HostedZoneId and DNSName , and if the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set EvaluateTargetHealth to true and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Amazon Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single Amazon EC2 instance, there are no special requirements.
            If you specify an ELB load balancer in `` AliasTarget `` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If no Amazon EC2 instances are healthy or if the load balancer itself is unhealthy, and if EvaluateTargetHealth is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources. When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the Amazon EC2 instances that you register with an ELB load balancer. For more information, see How Health Checks Work in More Complex Amazon Route 53 Configurations in the Amazon Route 53 Developers Guide .
            We recommend that you set EvaluateTargetHealth to true only when you have enough idle capacity to handle the failure of one or more endpoints.
            For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
            HealthCheckId (string) --If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the HealthCheckId element and specify the ID of the applicable health check.
            Amazon Route 53 determines whether a resource record set is healthy based on one of the following:
            By periodically sending a request to the endpoint that is specified in the health check
            By aggregating the status of a specified group of health checks (calculated health checks)
            By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)
            For information about how Amazon Route 53 determines whether a health check is healthy, see CreateHealthCheck .
            The HealthCheckId element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:
            You're checking the health of the resource record sets in a weighted, latency, geolocation, or failover resource record set, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set.
            You set EvaluateTargetHealth to true for the resource record sets in an alias, weighted alias, latency alias, geolocation alias, or failover alias resource record set, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets.
            Warning
            Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check.
            For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of CountryCode is * ), in that order, until it finds a resource record set for which the endpoint is healthy.
            If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com . For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com ), not the name of the resource record sets (example.com).
            Warning
            n this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.
            For more information, see the following topics in the Amazon Route 53 Developer Guide :
            Amazon Route 53 Health Checks and DNS Failover
            Configuring Failover in a Private Hosted Zone
            TrafficPolicyInstanceId (string) --When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Amazon Route 53 created this resource record set for.
            Warning
            To delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.
            
            
            

    :rtype: dict
    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    :returns: 
    HostedZoneId (string) -- [REQUIRED]
    The ID of the hosted zone that contains the resource record sets that you want to change.
    
    ChangeBatch (dict) -- [REQUIRED]
    A complex type that contains an optional comment and the Changes element.
    
    Comment (string) --
    Optional: Any comments you want to include about a change batch request.
    
    Changes (list) -- [REQUIRED]Information about the changes to make to the record sets.
    
    (dict) --The information for each resource record set that you want to change.
    
    Action (string) -- [REQUIRED]The action to perform:
    
    CREATE : Creates a resource record set that has the specified values.
    DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
    
    
    Warning
    To delete the resource record set that is associated with a traffic policy instance, use ``  DeleteTrafficPolicyInstance `` . Amazon Route 53will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.
    
    
    UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
    
    
    ResourceRecordSet (dict) -- [REQUIRED]Information about the resource record set to create or delete.
    
    Name (string) -- [REQUIRED]The name of the domain you want to perform the action on.
    Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
    For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
    You can use the asterisk (*) wildcard to replace the leftmost label in a domain name. For example, *.example.com . Note the following:
    
    The * must replace the entire label. For example, you can't specify *prod.example.com or prod*.example.com .
    The * can't replace any of the middle labels, for example, marketing.*.example.com.
    If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
    
    
    Warning
    You can't use the * wildcard for resource records sets that have a type of NS.
    
    You can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You cannot use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can't specify prod*.example.com .
    
    Type (string) -- [REQUIRED]The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
    Valid values for basic resource record sets: A | AAAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
    Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
    
    Note
    SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, The SPF DNS Record Type .
    
    Values for alias resource record sets:
    
    CloudFront distributions: A
    Elastic Beanstalk environment that has a regionalized subdomain : A
    ELB load balancers: A | AAAA
    Amazon S3 buckets: A
    Another resource record set in this hosted zone: Specify the type of the resource record set for which you're creating the alias. Specify any value except NS or SOA .
    
    
    SetIdentifier (string) --
    Weighted, Latency, Geo, and Failover resource record sets only: An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of SetIdentifier must be unique for each resource record set that has the same combination of DNS name and type. Omit SetIdentifier for any other types of record sets.
    
    Weight (integer) --
    Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:
    
    You must specify a value for the Weight element for every weighted resource record set.
    You can only specify one ResourceRecord per weighted resource record set.
    You cannot create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
    You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
    For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .
    
    
    Region (string) --
    Latency-based resource record sets only: The Amazon EC2 region where the resource that is specified in this resource record set resides. The resource typically is an AWS resource, such as an Amazon EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
    
    Note
    Creating latency and latency alias resource record sets in private hosted zones is not supported.
    
    When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 region. Amazon Route 53 then returns the value that is associated with the selected resource record set.
    Note the following:
    
    You can only specify one ResourceRecord per latency resource record set.
    You can only create one latency resource record set for each Amazon EC2 region.
    You are not required to create latency resource record sets for all Amazon EC2 regions. Amazon Route 53 will choose the region with the best latency from among the regions for which you create latency resource record sets.
    You cannot create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.
    
    
    GeoLocation (dict) --
    Geo location resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .
    
    Note
    Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.
    
    If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
    You cannot create two geolocation resource record sets that specify the same geographic location.
    The value * in the CountryCode element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the Name and Type elements.
    
    Warning
    Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of CountryCode is * , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a * resource record set, Amazon Route 53 returns a "no answer" response for queries from those locations.
    
    You cannot create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.
    
    ContinentCode (string) --The two-letter code for the continent.
    Valid values: AF | AN | AS | EU | OC | NA | SA
    Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
    
    CountryCode (string) --The two-letter code for the country.
    
    SubdivisionCode (string) --The code for the subdivision, for example, a state in the United States or a province in Canada.
    
    
    
    Failover (string) --
    Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
    Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:
    
    When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
    When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
    When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
    If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.
    
    You cannot create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
    For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
    For more information about configuring failover for Amazon Route 53, see the following topics in the Amazon Route 53 Developer Guide :
    
    Amazon Route 53 Health Checks and DNS Failover
    Configuring Failover in a Private Hosted Zone
    
    Valid values: PRIMARY | SECONDARY
    
    TTL (integer) --The resource record cache time to live (TTL), in seconds. Note the following:
    
    If you're creating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
    If you're associating this resource record set with a health check (if you're adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
    All of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets must have the same value for TTL .
    If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .
    
    
    ResourceRecords (list) --Information about the resource records to act upon.
    
    Note
    If you are creating an alias resource record set, omit ResourceRecords .
    
    
    (dict) --Information specific to the resource record.
    
    Note
    If you are creating an alias resource record set, omit ResourceRecord .
    
    
    Value (string) -- [REQUIRED]The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
    You can specify more than one value for all record types except CNAME and SOA .
    
    Note
    If you are creating an alias resource record set, omit Value .
    
    
    
    
    
    
    AliasTarget (dict) --
    Alias resource record sets only: Information about the CloudFront distribution, Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you are redirecting queries. The Elastic Beanstalk environment must have a regionalized subdomain.
    If you're creating resource records sets for a private hosted zone, note the following:
    
    You can't create alias resource record sets for CloudFront distributions in a private hosted zone.
    Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.
    For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .
    
    
    HostedZoneId (string) -- [REQUIRED]
    Alias resource records sets only : The value used depends on where the queries are routed:
    A CloudFront distribution
    
    Specify Z2FDTNDATAQYW2 .
    
    Note
    Alias resource record sets for CloudFront cannot be created in a private zone.
    Elastic Beanstalk environment
    
    Specify the hosted zone ID for the region in which you created the environment. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see AWS Elastic Beanstalk in the Regions and Endpoints chapter of the AWS General Reference .
    
    ELB load balancer
    Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
    
    AWS Management Console: Go to the Amazon EC2; page, click Load Balancers in the navigation pane, select the load balancer, and get the value of the Hosted Zone ID field on the Description tab. Use the same process to get the DNS Name. See  HostedZone$Name .
    Elastic Load Balancing API: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneNameID . Use the same process to get the CanonicalHostedZoneName . See  HostedZone$Name .
    AWS CLI: Use `` describe-load-balancers `` to get the value of CanonicalHostedZoneNameID . Use the same process to get the CanonicalHostedZoneName . See  HostedZone$Name .An Amazon S3 bucket configured as a static website
    
    
    Specify the hosted zone ID for the Amazon S3 website endpoint in which you created the bucket. For more information about valid values, see the table Amazon S3 (S3) Website Endpoints in the Amazon Web Services General Reference .
    
    Another Amazon Route 53 resource record set in your hosted zone
    Specify the hosted zone ID of your hosted zone. (An alias resource record set cannot reference a resource record set in a different hosted zone.)
    
    DNSName (string) -- [REQUIRED]
    Alias resource record sets only: The value that you specify depends on where you want to route queries:
    
    A CloudFront distribution: Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
    Elastic Beanstalk environment : Specify the CNAME attribute for the environment. (The environment must have a regionalized domain name.) You can use the following methods to get the value of the CNAME attribute:
    AWS Managment Console : For information about how to get the value by using the console, see Using Custom Domains with Elastic Beanstalk in the AWS Elastic Beanstalk Developer Guide .
    Elastic Load Balancing API : Use the DescribeEnvironments action to get the value of the CNAME attribute. For more information, see DescribeEnvironments in the AWS Elastic Beanstalk API Reference .
    AWS CLI : Use the describe-environments command to get the value of the CNAME attribute. For more information, see describe-environments in the AWS Command Line Interface Reference .
    
    
    An ELB load balancer: Specify the DNS name associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
    AWS Management Console : Go to the Amazon EC2 page, click Load Balancers in the navigation pane, choose the load balancer, choose the Description tab, and get the value of the DNS Name field that begins with dualstack. Use the same process to get the Hosted Zone ID. See  HostedZone$Id .
    Elastic Load Balancing API : Use `` DescribeLoadBalancers `` to get the value of CanonicalHostedZoneName . Use the same process to get the CanonicalHostedZoneNameId . See  HostedZone$Id .
    AWS CLI : Use `` describe-load-balancers `` to get the value of CanonicalHostedZoneName . Use the same process to get the CanonicalHostedZoneNameId . See HostedZoneId.
    
    
    An Amazon S3 bucket that is configured as a static website: Specify the domain name of the Amazon S3 website endpoint in which you created the bucket; for example, s3-website-us-east-1.amazonaws.com . For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference . For more information about using Amazon S3 buckets for websites, see Hosting a Static Website on Amazon S3 in the Amazon Simple Storage Service Developer Guide.
    Another Amazon Route 53 resource record set : Specify the value of the Name element for a resource record set in the current hosted zone.
    
    
    EvaluateTargetHealth (boolean) -- [REQUIRED]
    Applies only to alias, weighted alias, latency alias, and failover alias record sets: If you set the value of EvaluateTargetHealth to true for the resource record set or sets in an alias, weighted alias, latency alias, or failover alias resource record set, and if you specify a value for ``  HealthCheck$Id `` for every resource record set that is referenced by these alias resource record sets, the alias resource record sets inherit the health of the referenced resource record sets.
    In this configuration, when Amazon Route 53 receives a DNS query for an alias resource record set:
    
    Amazon Route 53 looks at the resource record sets that are referenced by the alias resource record sets to determine which health checks they're using.
    Amazon Route 53 checks the current status of each health check. (Amazon Route 53 periodically checks the health of the endpoint that is specified in a health check; it doesn't perform the health check when the DNS query arrives.)
    Based on the status of the health checks, Amazon Route 53 determines which resource record sets are healthy. Unhealthy resource record sets are immediately removed from consideration. In addition, if all of the resource record sets that are referenced by an alias resource record set are unhealthy, that alias resource record set also is immediately removed from consideration.
    Based on the configuration of the alias resource record sets (weighted alias or latency alias, for example) and the configuration of the resource record sets that they reference, Amazon Route 53 chooses a resource record set from the healthy resource record sets, and responds to the query.
    
    Note the following:
    
    You cannot set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.
    If the AWS resource that you specify in AliasTarget is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target.For more information, see What Happens When You Omit Health Checks? in the Amazon Route 53 Developer Guide .
    If you specify an Elastic Beanstalk environment in HostedZoneId and DNSName , and if the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set EvaluateTargetHealth to true and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Amazon Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single Amazon EC2 instance, there are no special requirements.
    If you specify an ELB load balancer in ``  AliasTarget `` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If no Amazon EC2 instances are healthy or if the load balancer itself is unhealthy, and if EvaluateTargetHealth is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources. When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the Amazon EC2 instances that you register with an ELB load balancer. For more information, see How Health Checks Work in More Complex Amazon Route 53 Configurations in the Amazon Route 53 Developers Guide .
    We recommend that you set EvaluateTargetHealth to true only when you have enough idle capacity to handle the failure of one or more endpoints.
    
    For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
    
    
    
    HealthCheckId (string) --If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the HealthCheckId element and specify the ID of the applicable health check.
    Amazon Route 53 determines whether a resource record set is healthy based on one of the following:
    
    By periodically sending a request to the endpoint that is specified in the health check
    By aggregating the status of a specified group of health checks (calculated health checks)
    By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)
    
    For information about how Amazon Route 53 determines whether a health check is healthy, see  CreateHealthCheck .
    The HealthCheckId element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:
    
    You're checking the health of the resource record sets in a weighted, latency, geolocation, or failover resource record set, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set.
    You set EvaluateTargetHealth to true for the resource record sets in an alias, weighted alias, latency alias, geolocation alias, or failover alias resource record set, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets.
    
    
    Warning
    Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check.
    
    For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of CountryCode is * ), in that order, until it finds a resource record set for which the endpoint is healthy.
    If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com . For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com ), not the name of the resource record sets (example.com).
    
    Warning
    n this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.
    
    For more information, see the following topics in the Amazon Route 53 Developer Guide :
    
    Amazon Route 53 Health Checks and DNS Failover
    Configuring Failover in a Private Hosted Zone
    
    
    TrafficPolicyInstanceId (string) --When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Amazon Route 53 created this resource record set for.
    
    Warning
    To delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def change_tags_for_resource(ResourceType=None, ResourceId=None, AddTags=None, RemoveTagKeys=None):
    """
    Adds, edits, or deletes tags for a health check or a hosted zone.
    For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    
    :example: response = client.change_tags_for_resource(
        ResourceType='healthcheck'|'hostedzone',
        ResourceId='string',
        AddTags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        RemoveTagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the resource.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource for which you want to add, change, or delete tags.
            

    :type AddTags: list
    :param AddTags: A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags for which you want to edit the Value element.
            You can add a maximum of 10 tags to a health check or a hosted zone.
            (dict) --A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.
            Key (string) --The value of Key depends on the operation that you want to perform:
            Add a tag to a health check or hosted zone : Key is the name that you want to give the new tag.
            Edit a tag : Key is the name of the tag whose Value element you want to remove.
            Delete a key : Key is the name of the tag you want to remove.
            Give a name to a health check : Edit the default Name tag. In the Amazon Route 53 console, the list of your health checks includes a Name column that lets you see the name that you've given to each health check.
            Value (string) --The value of Value depends on the operation that you want to perform:
            Add a tag to a health check or hosted zone : Value is the value that you want to give the new tag.
            Edit a tag : Value is the new value that you want to assign the tag.
            
            

    :type RemoveTagKeys: list
    :param RemoveTagKeys: A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_health_check(CallerReference=None, HealthCheckConfig=None):
    """
    Creates a new health check.
    To create a new health check, send a POST request to the /2013-04-01/healthcheck resource. The request body must include an XML document with a CreateHealthCheckRequest element. The response returns the CreateHealthCheckResponse element, containing the health check ID specified when adding health check to a resource record set. For information about adding health checks to resource record sets, see  ResourceRecordSet$HealthCheckId in  ChangeResourceRecordSets .
    If you are registering Amazon EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the Amazon EC2 instances. When you register an Amazon EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to an Amazon Route 53 health check.
    You can associate health checks with failover resource record sets in a private hosted zone. Note the following:
    
    
    :example: response = client.create_health_check(
        CallerReference='string',
        HealthCheckConfig={
            'IPAddress': 'string',
            'Port': 123,
            'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
            'ResourcePath': 'string',
            'FullyQualifiedDomainName': 'string',
            'SearchString': 'string',
            'RequestInterval': 123,
            'FailureThreshold': 123,
            'MeasureLatency': True|False,
            'Inverted': True|False,
            'HealthThreshold': 123,
            'ChildHealthChecks': [
                'string',
            ],
            'EnableSNI': True|False,
            'Regions': [
                'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
            ],
            'AlarmIdentifier': {
                'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                'Name': 'string'
            },
            'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
        }
    )
    
    
    :type CallerReference: string
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHealthCheck requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a health check.
            

    :type HealthCheckConfig: dict
    :param HealthCheckConfig: [REQUIRED]
            A complex type that contains the response to a CreateHealthCheck request.
            IPAddress (string) --The IPv4 IP address of the endpoint on which you want Amazon Route 53 to perform health checks. If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval. Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            If the endpoint is an Amazon EC2 instance, we recommend that you create an Elastic IP address, associate it with your Amazon EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
            For more information, see HealthCheckConfig$FullyQualifiedDomainName .
            Contraints: Amazon Route 53 cannot check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you cannot create health checks, see RFC 5735, Special Use IPv4 Addresses and RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space .
            When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress.
            Port (integer) --The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for Port only when you specify a value for IPAddress .
            Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.
            Warning
            You can't change the value of Type after you create a health check.
            You can create the following types of health checks:
            HTTP : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
            HTTPS : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
            Warning
            If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
            HTTP_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
            HTTPS_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
            TCP : Amazon Route 53 tries to establish a TCP connection.
            CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
            CALCULATED : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .
            For more information about how Amazon Route 53 determines whether an endpoint is healthy, see the introduction to this topic.
            ResourcePath (string) --The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html.
            FullyQualifiedDomainName (string) --Amazon Route 53 behavior depends on whether you specify a value for IPAddress .
            If you specify IPAddress :
            The value that you want Amazon Route 53 to pass in the Host header in all health checks except TCP health checks. This is typically the fully qualified DNS name of the website that you are attempting to health check. When Amazon Route 53 checks the health of an endpoint, here is how it constructs the Host header:
            If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
            If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
            If you specify another value for Port and any value except TCP for Type , Amazon Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.
            If you don't specify a value for FullyQualifiedDomainName , Amazon Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.
            If you don't specify IPAddress :
            If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to the domain that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com), not the name of the resource record sets (www.example.com).
            Warning
            In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
            In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Amazon Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Amazon Route 53 doesn't pass a Host header.
            SearchString (string) --If the value of Type is HTTP_STR_MATCH or HTTP_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.
            Amazon Route 53 considers case when searching for SearchString in the response body.
            RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request. Each Amazon Route 53 health checker makes requests at this interval.
            Warning
            You can't change the value of RequestInterval after you create a health check.
            FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
            MeasureLatency (boolean) --Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Amazon Route 53 console.
            Warning
            You can't change the value of MeasureLatency after you create a health check.
            Inverted (boolean) --Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
            HealthThreshold (integer) --The number of child health checks that are associated with a CALCULATED health that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the HealthCheckConfig$ChildHealthChecks and HealthCheckConfig$ChildHealthChecks elements.
            Note the following:
            If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy.
            If you specify 0 , Amazon Route 53 always considers this health check to be healthy.
            ChildHealthChecks (list) --(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.
            (string) --
            EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
            Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don't enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
            The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.
            Regions (list) --A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            AlarmIdentifier (dict) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            Region (string) -- [REQUIRED]A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            For the current list of CloudWatch regions, see Amazon CloudWatch in AWS Regions and Endpoints in the Amazon Web Services General Reference .
            Name (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            InsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
            Healthy : Amazon Route 53 considers the health check to be healthy.
            Unhealthy : Amazon Route 53 considers the health check to be unhealthy.
            LastKnownStatus : Amazon Route 53uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
            

    :rtype: dict
    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'HealthCheckConfig': {
                'IPAddress': 'string',
                'Port': 123,
                'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                'ResourcePath': 'string',
                'FullyQualifiedDomainName': 'string',
                'SearchString': 'string',
                'RequestInterval': 123,
                'FailureThreshold': 123,
                'MeasureLatency': True|False,
                'Inverted': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                    'Name': 'string'
                },
                'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
            },
            'HealthCheckVersion': 123,
            'CloudWatchAlarmConfiguration': {
                'EvaluationPeriods': 123,
                'Threshold': 123.0,
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'Period': 123,
                'MetricName': 'string',
                'Namespace': 'string',
                'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            }
        },
        'Location': 'string'
    }
    
    
    :returns: 
    CallerReference (string) -- [REQUIRED]
    A unique string that identifies the request and that allows failed CreateHealthCheck requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a health check.
    
    HealthCheckConfig (dict) -- [REQUIRED]
    A complex type that contains the response to a CreateHealthCheck request.
    
    IPAddress (string) --The IPv4 IP address of the endpoint on which you want Amazon Route 53 to perform health checks. If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval. Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
    If the endpoint is an Amazon EC2 instance, we recommend that you create an Elastic IP address, associate it with your Amazon EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
    For more information, see  HealthCheckConfig$FullyQualifiedDomainName .
    Contraints: Amazon Route 53 cannot check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you cannot create health checks, see RFC 5735, Special Use IPv4 Addresses and RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space .
    When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress.
    
    Port (integer) --The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for Port only when you specify a value for IPAddress .
    
    Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.
    
    Warning
    You can't change the value of Type after you create a health check.
    
    You can create the following types of health checks:
    
    HTTP : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    
    Warning
    If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
    
    
    HTTP_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    HTTPS_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    TCP : Amazon Route 53 tries to establish a TCP connection.
    CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
    CALCULATED : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .
    
    For more information about how Amazon Route 53 determines whether an endpoint is healthy, see the introduction to this topic.
    
    ResourcePath (string) --The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html.
    
    FullyQualifiedDomainName (string) --Amazon Route 53 behavior depends on whether you specify a value for IPAddress .
    
    If you specify IPAddress :
    The value that you want Amazon Route 53 to pass in the Host header in all health checks except TCP health checks. This is typically the fully qualified DNS name of the website that you are attempting to health check. When Amazon Route 53 checks the health of an endpoint, here is how it constructs the Host header:
    
    If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
    If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
    If you specify another value for Port and any value except TCP for Type , Amazon Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.
    
    If you don't specify a value for FullyQualifiedDomainName , Amazon Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.
    
    If you don't specify IPAddress :
    If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to the domain that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
    If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com), not the name of the resource record sets (www.example.com).
    
    Warning
    In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
    
    In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Amazon Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Amazon Route 53 doesn't pass a Host header.
    
    SearchString (string) --If the value of Type is HTTP_STR_MATCH or HTTP_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy.
    Amazon Route 53 considers case when searching for SearchString in the response body.
    
    RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request. Each Amazon Route 53 health checker makes requests at this interval.
    
    Warning
    You can't change the value of RequestInterval after you create a health check.
    
    
    FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
    
    MeasureLatency (boolean) --Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Amazon Route 53 console.
    
    Warning
    You can't change the value of MeasureLatency after you create a health check.
    
    
    Inverted (boolean) --Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
    
    HealthThreshold (integer) --The number of child health checks that are associated with a CALCULATED health that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.
    Note the following:
    
    If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy.
    If you specify 0 , Amazon Route 53 always considers this health check to be healthy.
    
    
    ChildHealthChecks (list) --(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.
    
    (string) --
    
    
    EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
    Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don't enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
    The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.
    
    Regions (list) --A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
    
    (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
    
    
    
    AlarmIdentifier (dict) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
    
    Region (string) -- [REQUIRED]A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
    For the current list of CloudWatch regions, see Amazon CloudWatch in AWS Regions and Endpoints in the Amazon Web Services General Reference .
    
    Name (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
    
    
    
    InsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
    
    Healthy : Amazon Route 53 considers the health check to be healthy.
    Unhealthy : Amazon Route 53 considers the health check to be unhealthy.
    LastKnownStatus : Amazon Route 53uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
    
    
    
    
    
    """
    pass

def create_hosted_zone(Name=None, VPC=None, CallerReference=None, HostedZoneConfig=None, DelegationSetId=None):
    """
    Creates a new public hosted zone, used to specify how the Domain Name System (DNS) routes traffic on the Internet for a domain, such as example.com, and its subdomains.
    Send a POST request to the /2013-04-01/hostedzone resource. The request body must include an XML document with a CreateHostedZoneRequest element. The response returns the CreateHostedZoneResponse element containing metadata about the hosted zone.
    Fore more information about charges for hosted zones, see Amazon Route 53 Pricing .
    Note the following:
    After creating a zone, its initial status is PENDING . This means that it is not yet available on all DNS servers. The status of the zone changes to INSYNC when the NS and SOA records are available on all Amazon Route 53 DNS servers.
    When trying to create a hosted zone using a reusable delegation set, specify an optional DelegationSetId, and Amazon Route 53 would assign those 4 NS records for the zone, instead of allotting a new one.
    
    
    :example: response = client.create_hosted_zone(
        Name='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
            'VPCId': 'string'
        },
        CallerReference='string',
        HostedZoneConfig={
            'Comment': 'string',
            'PrivateZone': True|False
        },
        DelegationSetId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Amazon Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in the DelegationSet element.
            

    :type VPC: dict
    :param VPC: The VPC that you want your hosted zone to be associated with. By providing this parameter, your newly created hosted cannot be resolved anywhere other than the given VPC.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            

    :type CallerReference: string
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a hosted zone. CallerReference can be any unique string, for example, a date/time stamp.
            

    :type HostedZoneConfig: dict
    :param HostedZoneConfig: (Optional) A complex type that contains an optional comment about your hosted zone. If you don't want to specify a comment, omit both the HostedZoneConfig and Comment elements.
            Comment (string) --Any comments that you want to include about the hosted zone.
            PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.
            

    :type DelegationSetId: string
    :param DelegationSetId: If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see CreateReusableDelegationSet .
            Type
            String
            Default
            None
            Parent
            CreatedHostedZoneRequest
            

    :rtype: dict
    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123
        },
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        },
        'DelegationSet': {
            'Id': 'string',
            'CallerReference': 'string',
            'NameServers': [
                'string',
            ]
        },
        'VPC': {
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
            'VPCId': 'string'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
    If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Amazon Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in the DelegationSet element.
    
    VPC (dict) -- The VPC that you want your hosted zone to be associated with. By providing this parameter, your newly created hosted cannot be resolved anywhere other than the given VPC.
    
    VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
    
    VPCId (string) --A VPC ID
    
    
    
    CallerReference (string) -- [REQUIRED]
    A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a hosted zone. CallerReference can be any unique string, for example, a date/time stamp.
    
    HostedZoneConfig (dict) -- (Optional) A complex type that contains an optional comment about your hosted zone. If you don't want to specify a comment, omit both the HostedZoneConfig and Comment elements.
    
    Comment (string) --Any comments that you want to include about the hosted zone.
    
    PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.
    
    
    
    DelegationSetId (string) -- If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see  CreateReusableDelegationSet .
    
    Type
    String
    
    Default
    None
    
    
    Parent
    CreatedHostedZoneRequest
    
    
    
    """
    pass

def create_reusable_delegation_set(CallerReference=None, HostedZoneId=None):
    """
    Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones. If a hosted zoned ID is specified, CreateReusableDelegationSet marks the delegation set associated with that zone as reusable
    Send a POST request to the /2013-04-01/delegationset resource. The request body must include an XML document with a CreateReusableDelegationSetRequest element.
    For more information, including a procedure on how to create and configure a reusable delegation set (also known as white label name servers), see Configuring White Label Name Servers .
    
    
    :example: response = client.create_reusable_delegation_set(
        CallerReference='string',
        HostedZoneId='string'
    )
    
    
    :type CallerReference: string
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example a date/time stamp.
            

    :type HostedZoneId: string
    :param HostedZoneId: If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.

    :rtype: dict
    :return: {
        'DelegationSet': {
            'Id': 'string',
            'CallerReference': 'string',
            'NameServers': [
                'string',
            ]
        },
        'Location': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_traffic_policy(Name=None, Document=None, Comment=None):
    """
    Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).
    Send a POST request to the /2013-04-01/trafficpolicy resource. The request body must include a document with a CreateTrafficPolicyRequest element. The response includes the CreateTrafficPolicyResponse element, which contains information about the new traffic policy.
    
    
    :example: response = client.create_traffic_policy(
        Name='string',
        Document='string',
        Comment='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the traffic policy.
            

    :type Document: string
    :param Document: [REQUIRED]
            The definition of this traffic policy in JSON format. For more information, see Traffic Policy Document Format in the Amazon Route 53 API Reference .
            

    :type Comment: string
    :param Comment: (Optional) Any comments that you want to include about the traffic policy.

    :rtype: dict
    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
            'Document': 'string',
            'Comment': 'string'
        },
        'Location': 'string'
    }
    
    
    """
    pass

def create_traffic_policy_instance(HostedZoneId=None, Name=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
    """
    Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, CreateTrafficPolicyInstance associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that CreateTrafficPolicyInstance created.
    Send a POST request to the /2013-04-01/trafficpolicyinstance resource. The request body must include a document with a CreateTrafficPolicyRequest element. The response returns the CreateTrafficPolicyInstanceResponse element, which contains information about the traffic policy instance.
    
    
    :example: response = client.create_traffic_policy_instance(
        HostedZoneId='string',
        Name='string',
        TTL=123,
        TrafficPolicyId='string',
        TrafficPolicyVersion=123
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone in which you want Amazon Route 53 to create resource record sets by using the configuration in a traffic policy.
            

    :type Name: string
    :param Name: [REQUIRED]
            The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Amazon Route 53 creates for this traffic policy instance.
            

    :type TTL: integer
    :param TTL: [REQUIRED]
            (Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.
            

    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            

    :rtype: dict
    :return: {
        'TrafficPolicyInstance': {
            'Id': 'string',
            'HostedZoneId': 'string',
            'Name': 'string',
            'TTL': 123,
            'State': 'string',
            'Message': 'string',
            'TrafficPolicyId': 'string',
            'TrafficPolicyVersion': 123,
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
        },
        'Location': 'string'
    }
    
    
    """
    pass

def create_traffic_policy_version(Id=None, Document=None, Comment=None):
    """
    Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you'll need to start a new traffic policy.
    Send a POST request to the /2013-04-01/trafficpolicy/ resource. The request body includes a document with a CreateTrafficPolicyVersionRequest element. The response returns the CreateTrafficPolicyVersionResponse element, which contains information about the new version of the traffic policy.
    
    
    :example: response = client.create_traffic_policy_version(
        Id='string',
        Document='string',
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy for which you want to create a new version.
            

    :type Document: string
    :param Document: [REQUIRED]
            The definition of this version of the traffic policy, in JSON format. You specified the JSON in the CreateTrafficPolicyVersion request. For more information about the JSON format, see CreateTrafficPolicy .
            

    :type Comment: string
    :param Comment: The comment that you specified in the CreateTrafficPolicyVersion request, if any.

    :rtype: dict
    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
            'Document': 'string',
            'Comment': 'string'
        },
        'Location': 'string'
    }
    
    
    """
    pass

def delete_health_check(HealthCheckId=None):
    """
    Deletes a health check. Send a DELETE request to the ``/2013-04-01/healthcheck/health check ID `` resource.
    
    
    :example: response = client.delete_health_check(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]
            The ID of the health check that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_hosted_zone(Id=None):
    """
    Deletes a hosted zone. Send a DELETE request to the ``/Amazon Route 53 API version /hostedzone/hosted zone ID `` resource.
    
    
    :example: response = client.delete_hosted_zone(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the hosted zone you want to delete.
            

    :rtype: dict
    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def delete_reusable_delegation_set(Id=None):
    """
    Deletes a reusable delegation set. Send a DELETE request to the ``/2013-04-01/delegationset/delegation set ID `` resource.
    To verify that the reusable delegation set is not associated with any hosted zones, run the  GetReusableDelegationSet action and specify the ID of the reusable delegation set that you want to delete.
    
    
    :example: response = client.delete_reusable_delegation_set(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the reusable delegation set you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_traffic_policy(Id=None, Version=None):
    """
    Deletes a traffic policy.
    Send a DELETE request to the /*Amazon Route 53 API version* /trafficpolicy resource.
    
    
    :example: response = client.delete_traffic_policy(
        Id='string',
        Version=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy that you want to delete.
            

    :type Version: integer
    :param Version: [REQUIRED]
            The version number of the traffic policy that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_traffic_policy_instance(Id=None):
    """
    Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.
    Send a DELETE request to the ``/Amazon Route 53 API version /trafficpolicy/traffic policy instance ID `` resource.
    
    
    :example: response = client.delete_traffic_policy_instance(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to delete.
            Warning
            When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disassociate_vpc_from_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    Disassociates a VPC from a Amazon Route 53 private hosted zone.
    Send a POST request to the /2013-04-01/hostedzone/*hosted zone ID* /disassociatevpc resource. The request body must include an XML document with a DisassociateVPCFromHostedZoneRequest element. The response returns the DisassociateVPCFromHostedZoneResponse element.
    
    
    :example: response = client.disassociate_vpc_from_hosted_zone(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
            'VPCId': 'string'
        },
        Comment='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the VPC that you want to disassociate from an Amazon Route 53 hosted zone.
            

    :type VPC: dict
    :param VPC: [REQUIRED]
            A complex type containing information about the Amazon VPC that you're disassociating from the specified hosted zone.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            

    :type Comment: string
    :param Comment: Optional: A comment about the disassociation request.

    :rtype: dict
    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to
            ClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

    """
    pass

def get_change(Id=None):
    """
    Returns the current status of a change batch request. The status is one of the following values:
    
    
    :example: response = client.get_change(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the change batch request. The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.
            

    :rtype: dict
    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def get_change_details(Id=None):
    """
    Returns the status and changes of a change batch request.
    
    
    :example: response = client.get_change_details(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the change batch. This is the value that you specified in the change ID parameter when you submitted the request.
            

    :rtype: dict
    :return: {
        'ChangeBatchRecord': {
            'Id': 'string',
            'SubmittedAt': datetime(2015, 1, 1),
            'Status': 'PENDING'|'INSYNC',
            'Comment': 'string',
            'Submitter': 'string',
            'Changes': [
                {
                    'Action': 'CREATE'|'DELETE'|'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'string',
                        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                        'SetIdentifier': 'string',
                        'Weight': 123,
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                        'GeoLocation': {
                            'ContinentCode': 'string',
                            'CountryCode': 'string',
                            'SubdivisionCode': 'string'
                        },
                        'Failover': 'PRIMARY'|'SECONDARY',
                        'TTL': 123,
                        'ResourceRecords': [
                            {
                                'Value': 'string'
                            },
                        ],
                        'AliasTarget': {
                            'HostedZoneId': 'string',
                            'DNSName': 'string',
                            'EvaluateTargetHealth': True|False
                        },
                        'HealthCheckId': 'string',
                        'TrafficPolicyInstanceId': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
    
    """
    pass

def get_checker_ip_ranges():
    """
    Retrieves a list of the IP ranges used by Amazon Route 53 health checkers to check the health of your resources. Send a GET request to the /*Amazon Route 53 API version* /checkeripranges resource. Use these IP addresses to configure router and firewall rules to allow health checkers to check the health of your resources.
    
    
    :example: response = client.get_checker_ip_ranges()
    
    
    :rtype: dict
    :return: {
        'CheckerIpRanges': [
            'string',
        ]
    }
    
    
    """
    pass

def get_geo_location(ContinentCode=None, CountryCode=None, SubdivisionCode=None):
    """
    Retrieves a single geo location. Send a GET request to the /2013-04-01/geolocation resource with one of these options: continentcode | countrycode | countrycode and subdivisioncode.
    
    
    :example: response = client.get_geo_location(
        ContinentCode='string',
        CountryCode='string',
        SubdivisionCode='string'
    )
    
    
    :type ContinentCode: string
    :param ContinentCode: Amazon Route 53 supports the following continent codes:
            AF : Africa
            AN : Antarctica
            AS : Asia
            EU : Europe
            OC : Oceania
            NA : North America
            SA : South America
            

    :type CountryCode: string
    :param CountryCode: Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .

    :type SubdivisionCode: string
    :param SubdivisionCode: Amazon Route 53 uses the one- to three-letter subdivision codes that are specified in ISO standard 3166-1 alpha-2 . Amazon Route 53 doesn't support subdivision codes for all countries. If you specify SubdivisionCode , you must also specify CountryCode .

    :rtype: dict
    :return: {
        'GeoLocationDetails': {
            'ContinentCode': 'string',
            'ContinentName': 'string',
            'CountryCode': 'string',
            'CountryName': 'string',
            'SubdivisionCode': 'string',
            'SubdivisionName': 'string'
        }
    }
    
    
    """
    pass

def get_health_check(HealthCheckId=None):
    """
    Gets information about a specified health check. Send a GET request to the ``/2013-04-01/healthcheck/health check ID `` resource. For more information about using the console to perform this operation, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide.
    
    
    :example: response = client.get_health_check(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]
            The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
            

    :rtype: dict
    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'HealthCheckConfig': {
                'IPAddress': 'string',
                'Port': 123,
                'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                'ResourcePath': 'string',
                'FullyQualifiedDomainName': 'string',
                'SearchString': 'string',
                'RequestInterval': 123,
                'FailureThreshold': 123,
                'MeasureLatency': True|False,
                'Inverted': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                    'Name': 'string'
                },
                'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
            },
            'HealthCheckVersion': 123,
            'CloudWatchAlarmConfiguration': {
                'EvaluationPeriods': 123,
                'Threshold': 123.0,
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'Period': 123,
                'MetricName': 'string',
                'Namespace': 'string',
                'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    HTTP_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    HTTPS_STR_MATCH : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    TCP : Amazon Route 53 tries to establish a TCP connection.
    CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
    CALCULATED : For health checks that monitor the status of other health checks, Amazon Route 53 adds up the number of health checks that Amazon Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .
    
    """
    pass

def get_health_check_count():
    """
    To retrieve a count of all your health checks, send a GET request to the /2013-04-01/healthcheckcount resource.
    
    
    :example: response = client.get_health_check_count()
    
    
    :rtype: dict
    :return: {
        'HealthCheckCount': 123
    }
    
    
    """
    pass

def get_health_check_last_failure_reason(HealthCheckId=None):
    """
    If you want to learn why a health check is currently failing or why it failed most recently (if at all), you can get the failure reason for the most recent failure. Send a GET request to the /*Amazon Route 53 API version* /healthcheck/*health check ID* /lastfailurereason resource.
    
    
    :example: response = client.get_health_check_last_failure_reason(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]
            The ID for the health check for which you want the last failure reason. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.
            

    :rtype: dict
    :return: {
        'HealthCheckObservations': [
            {
                'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                'IPAddress': 'string',
                'StatusReport': {
                    'Status': 'string',
                    'CheckedTime': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    """
    pass

def get_health_check_status(HealthCheckId=None):
    """
    Gets status of a specified health check. Send a GET request to the /2013-04-01/healthcheck/*health check ID* /status resource. You can use this call to get a health check's current status.
    
    
    :example: response = client.get_health_check_status(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]
            If you want Amazon Route 53 to return this resource record set in response to a DNS query only when a health check is passing, include the HealthCheckId element and specify the ID of the applicable health check.
            Amazon Route 53 determines whether a resource record set is healthy by periodically sending a request to the endpoint that is specified in the health check. If that endpoint returns an HTTP status code of 2xx or 3xx, the endpoint is healthy. If the endpoint returns an HTTP status code of 400 or greater, or if the endpoint doesn't respond for a certain amount of time, Amazon Route 53 considers the endpoint unhealthy and also considers the resource record set unhealthy.
            The HealthCheckId element is only useful when Amazon Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Amazon Route 53 to base the choice in part on the status of a health check. Configuring health checks only makes sense in the following configurations:
            You're checking the health of the resource record sets in a weighted, latency, geolocation, or failover resource record set, and you specify health check IDs for all of the resource record sets. If the health check for one resource record set specifies an endpoint that is not healthy, Amazon Route 53 stops responding to queries using the value for that resource record set.
            You set EvaluateTargetHealth to true for the resource record sets in an alias, weighted alias, latency alias, geolocation alias, or failover alias resource record set, and you specify health check IDs for all of the resource record sets that are referenced by the alias resource record sets. For more information about this configuration, see EvaluateTargetHealth . Amazon Route 53 doesn't check the health of the endpoint specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Amazon Route 53 checks the health of the endpoint that you specified in the health check.
            For geolocation resource record sets, if an endpoint is unhealthy, Amazon Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the United States, for North America, and for all locations. If the endpoint for the state resource record set is unhealthy, Amazon Route 53 checks the resource record sets for the United States, for North America, and for all locations (a resource record set for which the value of CountryCode is * ), in that order, until it finds a resource record set for which the endpoint is healthy.
            If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com ), not the name of the resource record sets (example.com).
            Warning
            In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and then associate the health check with those resource record sets, health check results will be unpredictable.
            

    :rtype: dict
    :return: {
        'HealthCheckObservations': [
            {
                'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                'IPAddress': 'string',
                'StatusReport': {
                    'Status': 'string',
                    'CheckedTime': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    """
    pass

def get_hosted_zone(Id=None):
    """
    Retrieves the delegation set for a hosted zone, including the four name servers assigned to the hosted zone. Send a GET request to the ``/Amazon Route 53 API version /hostedzone/hosted zone ID `` resource.
    
    
    :example: response = client.get_hosted_zone(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the hosted zone for which you want to get a list of the name servers in the delegation set.
            

    :rtype: dict
    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123
        },
        'DelegationSet': {
            'Id': 'string',
            'CallerReference': 'string',
            'NameServers': [
                'string',
            ]
        },
        'VPCs': [
            {
                'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
                'VPCId': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_hosted_zone_count():
    """
    Retrieves a count of all your hosted zones. Send a GET request to the /2013-04-01/hostedzonecount resource.
    
    
    :example: response = client.get_hosted_zone_count()
    
    
    :rtype: dict
    :return: {
        'HostedZoneCount': 123
    }
    
    
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_reusable_delegation_set(Id=None):
    """
    Retrieves the reusable delegation set. Send a GET request to the ``/2013-04-01/delegationset/delegation set ID `` resource.
    
    
    :example: response = client.get_reusable_delegation_set(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the reusable delegation set for which you want to get a list of the name server.
            

    :rtype: dict
    :return: {
        'DelegationSet': {
            'Id': 'string',
            'CallerReference': 'string',
            'NameServers': [
                'string',
            ]
        }
    }
    
    
    """
    pass

def get_traffic_policy(Id=None, Version=None):
    """
    Gets information about a specific traffic policy version.
    Send a GET request to the /*Amazon Route 53 API version* /trafficpolicy resource.
    
    
    :example: response = client.get_traffic_policy(
        Id='string',
        Version=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy that you want to get information about.
            

    :type Version: integer
    :param Version: [REQUIRED]
            The version number of the traffic policy that you want to get information about.
            

    :rtype: dict
    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
            'Document': 'string',
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def get_traffic_policy_instance(Id=None):
    """
    Gets information about a specified traffic policy instance.
    Send a GET request to the /*Amazon Route 53 API version* /trafficpolicyinstance resource.
    
    
    :example: response = client.get_traffic_policy_instance(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to get information about.
            

    :rtype: dict
    :return: {
        'TrafficPolicyInstance': {
            'Id': 'string',
            'HostedZoneId': 'string',
            'Name': 'string',
            'TTL': 123,
            'State': 'string',
            'Message': 'string',
            'TrafficPolicyId': 'string',
            'TrafficPolicyVersion': 123,
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
        }
    }
    
    
    """
    pass

def get_traffic_policy_instance_count():
    """
    Gets the number of traffic policy instances that are associated with the current AWS account.
    To get the number of traffic policy instances, send a GET request to the /2013-04-01/trafficpolicyinstancecount resource.
    
    
    :example: response = client.get_traffic_policy_instance_count()
    
    
    :rtype: dict
    :return: {
        'TrafficPolicyInstanceCount': 123
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_change_batches_by_hosted_zone(HostedZoneId=None, StartDate=None, EndDate=None, MaxItems=None, Marker=None):
    """
    Gets the list of ChangeBatches in a given time period for a given hosted zone.
    
    
    :example: response = client.list_change_batches_by_hosted_zone(
        HostedZoneId='string',
        StartDate='string',
        EndDate='string',
        MaxItems='string',
        Marker='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want to see changes for.
            

    :type StartDate: string
    :param StartDate: [REQUIRED]
            The start of the time period you want to see changes for.
            

    :type EndDate: string
    :param EndDate: [REQUIRED]
            The end of the time period you want to see changes for.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of items on a page.

    :type Marker: string
    :param Marker: The page marker.

    :rtype: dict
    :return: {
        'MaxItems': 'string',
        'Marker': 'string',
        'IsTruncated': True|False,
        'ChangeBatchRecords': [
            {
                'Id': 'string',
                'SubmittedAt': datetime(2015, 1, 1),
                'Status': 'PENDING'|'INSYNC',
                'Comment': 'string',
                'Submitter': 'string',
                'Changes': [
                    {
                        'Action': 'CREATE'|'DELETE'|'UPSERT',
                        'ResourceRecordSet': {
                            'Name': 'string',
                            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                            'SetIdentifier': 'string',
                            'Weight': 123,
                            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                            'GeoLocation': {
                                'ContinentCode': 'string',
                                'CountryCode': 'string',
                                'SubdivisionCode': 'string'
                            },
                            'Failover': 'PRIMARY'|'SECONDARY',
                            'TTL': 123,
                            'ResourceRecords': [
                                {
                                    'Value': 'string'
                                },
                            ],
                            'AliasTarget': {
                                'HostedZoneId': 'string',
                                'DNSName': 'string',
                                'EvaluateTargetHealth': True|False
                            },
                            'HealthCheckId': 'string',
                            'TrafficPolicyInstanceId': 'string'
                        }
                    },
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    CREATE : Creates a resource record set that has the specified values.
    DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
    
    """
    pass

def list_change_batches_by_rr_set(HostedZoneId=None, Name=None, Type=None, SetIdentifier=None, StartDate=None, EndDate=None, MaxItems=None, Marker=None):
    """
    Gets the list of ChangeBatches in a given time period for a given hosted zone and RRSet.
    
    
    :example: response = client.list_change_batches_by_rr_set(
        HostedZoneId='string',
        Name='string',
        Type='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        SetIdentifier='string',
        StartDate='string',
        EndDate='string',
        MaxItems='string',
        Marker='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want to see changes for.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the RRSet that you want to see changes for.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of the RRSet that you want to see changes for.
            

    :type SetIdentifier: string
    :param SetIdentifier: The identifier of the RRSet that you want to see changes for.

    :type StartDate: string
    :param StartDate: [REQUIRED]
            The start of the time period you want to see changes for.
            

    :type EndDate: string
    :param EndDate: [REQUIRED]
            The end of the time period you want to see changes for.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of items on a page.

    :type Marker: string
    :param Marker: The page marker.

    :rtype: dict
    :return: {
        'MaxItems': 'string',
        'Marker': 'string',
        'IsTruncated': True|False,
        'ChangeBatchRecords': [
            {
                'Id': 'string',
                'SubmittedAt': datetime(2015, 1, 1),
                'Status': 'PENDING'|'INSYNC',
                'Comment': 'string',
                'Submitter': 'string',
                'Changes': [
                    {
                        'Action': 'CREATE'|'DELETE'|'UPSERT',
                        'ResourceRecordSet': {
                            'Name': 'string',
                            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                            'SetIdentifier': 'string',
                            'Weight': 123,
                            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                            'GeoLocation': {
                                'ContinentCode': 'string',
                                'CountryCode': 'string',
                                'SubdivisionCode': 'string'
                            },
                            'Failover': 'PRIMARY'|'SECONDARY',
                            'TTL': 123,
                            'ResourceRecords': [
                                {
                                    'Value': 'string'
                                },
                            ],
                            'AliasTarget': {
                                'HostedZoneId': 'string',
                                'DNSName': 'string',
                                'EvaluateTargetHealth': True|False
                            },
                            'HealthCheckId': 'string',
                            'TrafficPolicyInstanceId': 'string'
                        }
                    },
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    CREATE : Creates a resource record set that has the specified values.
    DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
    
    """
    pass

def list_geo_locations(StartContinentCode=None, StartCountryCode=None, StartSubdivisionCode=None, MaxItems=None):
    """
    Retrieves a list of supported geo locations. Send a GET request to the /2013-04-01/geolocations resource. The response to this request includes a GeoLocationDetailsList element for each location that Amazon Route 53 supports.
    Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.
    
    
    :example: response = client.list_geo_locations(
        StartContinentCode='string',
        StartCountryCode='string',
        StartSubdivisionCode='string',
        MaxItems='string'
    )
    
    
    :type StartContinentCode: string
    :param StartContinentCode: The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true, and if NextContinentCode from the previous response has a value, enter that value in StartContinentCode to return the next page of results.
            Include StartContinentCode only if you want to list continents. Don't include StartContinentCode when you're listing countries or countries with their subdivisions.
            

    :type StartCountryCode: string
    :param StartCountryCode: The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextCountryCode from the previous response has a value, enter that value in StartCountryCode to return the next page of results.
            Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .
            

    :type StartSubdivisionCode: string
    :param StartSubdivisionCode: The code for the subdivision (for example, state or province) with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextSubdivisionCode from the previous response has a value, enter that value in StartSubdivisionCode to return the next page of results.
            To list subdivisions of a country, you must include both StartCountryCode and StartSubdivisionCode .
            

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of geolocations to be included in the response body for this request. If more than MaxItems geolocations remain to be listed, then the value of the IsTruncated element in the response is true .

    :rtype: dict
    :return: {
        'GeoLocationDetailsList': [
            {
                'ContinentCode': 'string',
                'ContinentName': 'string',
                'CountryCode': 'string',
                'CountryName': 'string',
                'SubdivisionCode': 'string',
                'SubdivisionName': 'string'
            },
        ],
        'IsTruncated': True|False,
        'NextContinentCode': 'string',
        'NextCountryCode': 'string',
        'NextSubdivisionCode': 'string',
        'MaxItems': 'string'
    }
    
    
    """
    pass

def list_health_checks(Marker=None, MaxItems=None):
    """
    Retrieve a list of your health checks. Send a GET request to the /2013-04-01/healthcheck resource. The response to this request includes a HealthChecks element with zero or more HealthCheck child elements. By default, the list of health checks is displayed on a single page. You can control the length of the page that is displayed by using the MaxItems parameter. You can use the Marker parameter to control the health check that the list begins with.
    For information about listing health checks using the Amazon Route 53 console, see Amazon Route 53 Health Checks and DNS Failover .
    
    
    :example: response = client.list_health_checks(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: If the response to a ListHealthChecks is more than one page, marker is the health check ID for the first health check on the next page of results. For more information, see ListHealthChecksResponse$MaxItems .

    :type MaxItems: string
    :param MaxItems: The maximum number of HealthCheck elements you want ListHealthChecks to return on each page of the response body. If the AWS account includes more HealthCheck elements than the value of maxitems , the response is broken into pages. Each page contains the number of HealthCheck elements specified by maxitems .
            For example, suppose you specify 10 for maxitems and the current AWS account has 51 health checks. In the response, ListHealthChecks sets ListHealthChecksResponse$IsTruncated to true and includes the ListHealthChecksResponse$NextMarker element. To access the second and subsequent pages, you resend the GET ListHealthChecks request, add the ListHealthChecksResponse$Marker parameter to the request, and specify the value of the ListHealthChecksResponse$NextMarker element from the previous response. On the last (sixth) page of the response, which contains only one HealthCheck element:
            The value of ListHealthChecksResponse$IsTruncated is false .
            ListHealthChecksResponse$NextMarker is omitted.
            

    :rtype: dict
    :return: {
        'HealthChecks': [
            {
                'Id': 'string',
                'CallerReference': 'string',
                'HealthCheckConfig': {
                    'IPAddress': 'string',
                    'Port': 123,
                    'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                    'ResourcePath': 'string',
                    'FullyQualifiedDomainName': 'string',
                    'SearchString': 'string',
                    'RequestInterval': 123,
                    'FailureThreshold': 123,
                    'MeasureLatency': True|False,
                    'Inverted': True|False,
                    'HealthThreshold': 123,
                    'ChildHealthChecks': [
                        'string',
                    ],
                    'EnableSNI': True|False,
                    'Regions': [
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    ],
                    'AlarmIdentifier': {
                        'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                        'Name': 'string'
                    },
                    'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
                },
                'HealthCheckVersion': 123,
                'CloudWatchAlarmConfiguration': {
                    'EvaluationPeriods': 123,
                    'Threshold': 123.0,
                    'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                    'Period': 123,
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
        ],
        'Marker': 'string',
        'IsTruncated': True|False,
        'NextMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    HTTP : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    """
    pass

def list_hosted_zones(Marker=None, MaxItems=None, DelegationSetId=None):
    """
    To retrieve a list of your public and private hosted zones, send a GET request to the /2013-04-01/hostedzone resource. The response to this request includes a HostedZones child element for each hosted zone created by the current AWS account.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the maxitems parameter to list them in groups of up to 100. The response includes four values that help navigate from one group of maxitems hosted zones to the next:
    
    
    :example: response = client.list_hosted_zones(
        Marker='string',
        MaxItems='string',
        DelegationSetId='string'
    )
    
    
    :type Marker: string
    :param Marker: (Optional) If you have more hosted zones than the value of maxitems , ListHostedZones returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZones . For the value of marker, specify the value of the NextMarker element that was returned in the previous response.
            Hosted zones are listed in the order in which they were created.
            

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, the value of the IsTruncated element in the response is true , and the value of the NextMarker element is the hosted zone ID of the first hosted zone in the next group of maxitems hosted zones.

    :type DelegationSetId: string
    :param DelegationSetId: If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.

    :rtype: dict
    :return: {
        'HostedZones': [
            {
                'Id': 'string',
                'Name': 'string',
                'CallerReference': 'string',
                'Config': {
                    'Comment': 'string',
                    'PrivateZone': True|False
                },
                'ResourceRecordSetCount': 123
            },
        ],
        'Marker': 'string',
        'IsTruncated': True|False,
        'NextMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Marker (string) -- (Optional) If you have more hosted zones than the value of maxitems , ListHostedZones returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZones . For the value of marker, specify the value of the NextMarker element that was returned in the previous response.
    Hosted zones are listed in the order in which they were created.
    
    MaxItems (string) -- (Optional) The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, the value of the IsTruncated element in the response is true , and the value of the NextMarker element is the hosted zone ID of the first hosted zone in the next group of maxitems hosted zones.
    DelegationSetId (string) -- If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.
    
    """
    pass

def list_hosted_zones_by_name(DNSName=None, HostedZoneId=None, MaxItems=None):
    """
    Retrieves a list of your hosted zones in lexicographic order. Send a GET request to the /2013-04-01/hostedzonesbyname resource. The response includes a HostedZones child element for each hosted zone created by the current AWS account.
    Note the trailing dot, which can change the sort order in some circumstances.
    If the domain name includes escape characters or Punycode, ListHostedZonesByName alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for example.com, specify ex344mple.com for the domain name. ListHostedZonesByName alphabetizes it as:
    The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide.
    Amazon Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the MaxItems parameter to list them in groups of up to 100. The response includes values that help navigate from one group of MaxItems hosted zones to the next:
    
    
    :example: response = client.list_hosted_zones_by_name(
        DNSName='string',
        HostedZoneId='string',
        MaxItems='string'
    )
    
    
    :type DNSName: string
    :param DNSName: (Optional) For your first request to ListHostedZonesByName , include the dnsname parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the dnsname parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both dnsname and hostedzoneid parameters. For dnsname , specify the value of NextDNSName from the previous response.

    :type HostedZoneId: string
    :param HostedZoneId: (Optional) For your first request to ListHostedZonesByName , do not include the hostedzoneid parameter.
            If you have more hosted zones than the value of maxitems , ListHostedZonesByName returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZonesByName and include both dnsname and hostedzoneid parameters. For the value of hostedzoneid , specify the value of the NextHostedZoneId element from the previous response.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, then the value of the IsTruncated element in the response is true, and the values of NextDNSName and NextHostedZoneId specify the first hosted zone in the next group of maxitems hosted zones.

    :rtype: dict
    :return: {
        'HostedZones': [
            {
                'Id': 'string',
                'Name': 'string',
                'CallerReference': 'string',
                'Config': {
                    'Comment': 'string',
                    'PrivateZone': True|False
                },
                'ResourceRecordSetCount': 123
            },
        ],
        'DNSName': 'string',
        'HostedZoneId': 'string',
        'IsTruncated': True|False,
        'NextDNSName': 'string',
        'NextHostedZoneId': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    com.ex\344mple.
    
    """
    pass

def list_resource_record_sets(HostedZoneId=None, StartRecordName=None, StartRecordType=None, StartRecordIdentifier=None, MaxItems=None):
    """
    Lists the resource record sets in a specified hosted zone.
    Note the trailing dot, which can change the sort order in some circumstances.
    When multiple records have the same DNS name, the action sorts results by the record type.
    You can use the name and type elements to adjust the beginning position of the list of resource record sets returned:
    The results begin with the first resource record set that the hosted zone contains.
    The results begin with the first resource record set in the list whose name is greater than or equal to Name .
    Amazon Route 53 returns the InvalidInput error.
    The results begin with the first resource record set in the list whose name is greater than or equal to Name , and whose type is greater than or equal to Type .
    This action returns the most current version of the records. This includes records that are PENDING , and that are not yet available on all Amazon Route 53 DNS servers.
    To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a ChangeResourceRecordSets request while you're paging through the results of a ListResourceRecordSets request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.
    
    
    :example: response = client.list_resource_record_sets(
        HostedZoneId='string',
        StartRecordName='string',
        StartRecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        StartRecordIdentifier='string',
        MaxItems='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to get.
            

    :type StartRecordName: string
    :param StartRecordName: The first name in the lexicographic ordering of domain names that you want the ListResourceRecordSets request to list.

    :type StartRecordType: string
    :param StartRecordType: The type of resource record set to begin the record listing from.
            Valid values for basic resource record sets: A | AAAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
            Values for weighted, latency, geo, and failover resource record sets: A | AAAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT
            Values for alias resource record sets:
            CloudFront distribution : A
            Elastic Beanstalk environment that has a regionalized subdomain : A
            ELB load balancer : A | AAAA
            Amazon S3 bucket : A
            Constraint: Specifying type without specifying name returns an InvalidInput error.
            

    :type StartRecordIdentifier: string
    :param StartRecordIdentifier: Weighted resource record sets only: If results were truncated for a given DNS name and type, specify the value of NextRecordIdentifier from the previous response to get the next resource record set that has the current DNS name and type.

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than maxitems resource record sets, the value of the IsTruncated element in the response is true , and the values of the NextRecordName and NextRecordType elements in the response identify the first resource record set in the next group of maxitems resource record sets.

    :rtype: dict
    :return: {
        'ResourceRecordSets': [
            {
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                'SetIdentifier': 'string',
                'Weight': 123,
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
                'GeoLocation': {
                    'ContinentCode': 'string',
                    'CountryCode': 'string',
                    'SubdivisionCode': 'string'
                },
                'Failover': 'PRIMARY'|'SECONDARY',
                'TTL': 123,
                'ResourceRecords': [
                    {
                        'Value': 'string'
                    },
                ],
                'AliasTarget': {
                    'HostedZoneId': 'string',
                    'DNSName': 'string',
                    'EvaluateTargetHealth': True|False
                },
                'HealthCheckId': 'string',
                'TrafficPolicyInstanceId': 'string'
            },
        ],
        'IsTruncated': True|False,
        'NextRecordName': 'string',
        'NextRecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        'NextRecordIdentifier': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    The * must replace the entire label. For example, you can't specify *prod.example.com or prod*.example.com .
    The * can't replace any of the middle labels, for example, marketing.*.example.com.
    If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
    
    """
    pass

def list_reusable_delegation_sets(Marker=None, MaxItems=None):
    """
    To retrieve a list of your reusable delegation sets, send a GET request to the /2013-04-01/delegationset resource. The response to this request includes a DelegationSets element with zero, one, or multiple DelegationSet child elements. By default, the list of delegation sets is displayed on a single page. You can control the length of the page that is displayed by using the MaxItems parameter. You can use the Marker parameter to control the delegation set that the list begins with.
    
    
    :example: response = client.list_reusable_delegation_sets(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: If you're making the second or subsequent call to ListReusableDelegationSets , the Marker element matches the value that you specified in the marker parameter in the previous request.

    :type MaxItems: string
    :param MaxItems: The value that you specified for the maxitems parameter in the request that produced the current response.

    :rtype: dict
    :return: {
        'DelegationSets': [
            {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                    'string',
                ]
            },
        ],
        'Marker': 'string',
        'IsTruncated': True|False,
        'NextMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceType=None, ResourceId=None):
    """
    Lists tags for one health check or hosted zone.
    For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    
    :example: response = client.list_tags_for_resource(
        ResourceType='healthcheck'|'hostedzone',
        ResourceId='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the resource.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource for which you want to retrieve tags.
            

    :rtype: dict
    :return: {
        'ResourceTagSet': {
            'ResourceType': 'healthcheck'|'hostedzone',
            'ResourceId': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    The resource type for health checks is healthcheck .
    The resource type for hosted zones is hostedzone .
    
    """
    pass

def list_tags_for_resources(ResourceType=None, ResourceIds=None):
    """
    Lists tags for up to 10 health checks or hosted zones.
    For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    
    :example: response = client.list_tags_for_resources(
        ResourceType='healthcheck'|'hostedzone',
        ResourceIds=[
            'string',
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the resources.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            

    :type ResourceIds: list
    :param ResourceIds: [REQUIRED]
            A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.
            (string) --
            

    :rtype: dict
    :return: {
        'ResourceTagSets': [
            {
                'ResourceType': 'healthcheck'|'hostedzone',
                'ResourceId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    The resource type for health checks is healthcheck .
    The resource type for hosted zones is hostedzone .
    
    """
    pass

def list_traffic_policies(TrafficPolicyIdMarker=None, MaxItems=None):
    """
    Gets information about the latest version for every traffic policy that is associated with the current AWS account. Send a GET request to the /*Amazon Route 53 API version* /trafficpolicy resource.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policies, you can use the maxitems parameter to list them in groups of up to 100.
    The response includes three values that help you navigate from one group of maxitems traffic policies to the next:
    
    
    :example: response = client.list_traffic_policies(
        TrafficPolicyIdMarker='string',
        MaxItems='string'
    )
    
    
    :type TrafficPolicyIdMarker: string
    :param TrafficPolicyIdMarker: (Conditional) For your first request to ListTrafficPolicies , do not include the TrafficPolicyIdMarker parameter.
            If you have more traffic policies than the value of MaxItems , ListTrafficPolicies returns only the first MaxItems traffic policies. To get the next group of MaxItems policies, submit another request to ListTrafficPolicies . For the value of TrafficPolicyIdMarker , specify the value of the TrafficPolicyIdMarker element that was returned in the previous response.
            Policies are listed in the order in which they were created.
            

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of traffic policies to be included in the response body for this request. If you have more than MaxItems traffic policies, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyIdMarker element is the ID of the first traffic policy in the next group of MaxItems traffic policies.

    :rtype: dict
    :return: {
        'TrafficPolicySummaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                'LatestVersion': 123,
                'TrafficPolicyCount': 123
            },
        ],
        'IsTruncated': True|False,
        'TrafficPolicyIdMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    TrafficPolicyIdMarker (string) -- (Conditional) For your first request to ListTrafficPolicies , do not include the TrafficPolicyIdMarker parameter.
    If you have more traffic policies than the value of MaxItems , ListTrafficPolicies returns only the first MaxItems traffic policies. To get the next group of MaxItems policies, submit another request to ListTrafficPolicies . For the value of TrafficPolicyIdMarker , specify the value of the TrafficPolicyIdMarker element that was returned in the previous response.
    Policies are listed in the order in which they were created.
    
    MaxItems (string) -- (Optional) The maximum number of traffic policies to be included in the response body for this request. If you have more than MaxItems traffic policies, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyIdMarker element is the ID of the first traffic policy in the next group of MaxItems traffic policies.
    
    """
    pass

def list_traffic_policy_instances(HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created by using the current AWS account.
    Send a GET request to the /*Amazon Route 53 API version* /trafficpolicyinstance resource.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    The response includes five values that help you navigate from one group of MaxItems traffic policy instances to the next:
    
    
    :example: response = client.list_traffic_policy_instances(
        HostedZoneIdMarker='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        MaxItems='string'
    )
    
    
    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get the next group of MaxItems traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of HostedZoneIdMarker , specify the value of HostedZoneIdMarker from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.

    :rtype: dict
    :return: {
        'TrafficPolicyInstances': [
            {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
            },
        ],
        'HostedZoneIdMarker': 'string',
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    HostedZoneIdMarker (string) -- For the first request to ListTrafficPolicyInstances , omit this value.
    If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get the next group of MaxItems traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of HostedZoneIdMarker , specify the value of HostedZoneIdMarker from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
    
    TrafficPolicyInstanceNameMarker (string) -- For the first request to ListTrafficPolicyInstances , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
    
    TrafficPolicyInstanceTypeMarker (string) -- For the first request to ListTrafficPolicyInstances , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
    
    MaxItems (string) -- The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
    
    """
    pass

def list_traffic_policy_instances_by_hosted_zone(HostedZoneId=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created in a specified hosted zone.
    Send a GET request to the /*Amazon Route 53 API version* /trafficpolicyinstance resource and include the ID of the hosted zone.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    The response includes four values that help you navigate from one group of MaxItems traffic policy instances to the next:
    
    
    :example: response = client.list_traffic_policy_instances_by_hosted_zone(
        HostedZoneId='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        MaxItems='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone for which you want to list traffic policy instances.
            

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.

    :rtype: dict
    :return: {
        'TrafficPolicyInstances': [
            {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
            },
        ],
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    HostedZoneId (string) -- [REQUIRED]
    The ID of the hosted zone for which you want to list traffic policy instances.
    
    TrafficPolicyInstanceNameMarker (string) -- For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
    If the value of IsTruncated in the previous response was false , omit this value.
    
    TrafficPolicyInstanceTypeMarker (string) -- For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
    
    MaxItems (string) -- The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
    
    """
    pass

def list_traffic_policy_instances_by_policy(TrafficPolicyId=None, TrafficPolicyVersion=None, HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created by using a specify traffic policy version.
    Send a GET request to the /*Route 53 API version* /trafficpolicyinstance resource and include the ID and version of the traffic policy.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    The response includes five values that help you navigate from one group of MaxItems traffic policy instances to the next:
    
    
    :example: response = client.list_traffic_policy_instances_by_policy(
        TrafficPolicyId='string',
        TrafficPolicyVersion=123,
        HostedZoneIdMarker='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        MaxItems='string'
    )
    
    
    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy for which you want to list traffic policy instances.
            

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by TrafficPolicyId .
            

    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , HostedZoneIdMarker is the ID of the hosted zone for the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.

    :rtype: dict
    :return: {
        'TrafficPolicyInstances': [
            {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
            },
        ],
        'HostedZoneIdMarker': 'string',
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    TrafficPolicyId (string) -- [REQUIRED]
    The ID of the traffic policy for which you want to list traffic policy instances.
    
    TrafficPolicyVersion (integer) -- [REQUIRED]
    The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by TrafficPolicyId .
    
    HostedZoneIdMarker (string) -- For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
    If the value of IsTruncated in the previous response was true , HostedZoneIdMarker is the ID of the hosted zone for the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
    If the value of IsTruncated in the previous response was false , omit this value.
    
    TrafficPolicyInstanceNameMarker (string) -- For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
    If the value of IsTruncated in the previous response was false , omit this value.
    
    TrafficPolicyInstanceTypeMarker (string) -- For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
    If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
    If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
    
    MaxItems (string) -- The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
    
    """
    pass

def list_traffic_policy_versions(Id=None, TrafficPolicyVersionMarker=None, MaxItems=None):
    """
    Gets information about all of the versions for a specified traffic policy.
    Send a GET request to the /*Amazon Route 53 API version* /trafficpolicy resource and specify the ID of the traffic policy for which you want to list versions.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policies, you can use the maxitems parameter to list them in groups of up to 100.
    The response includes three values that help you navigate from one group of maxitems traffic policies to the next:
    
    
    :example: response = client.list_traffic_policy_versions(
        Id='string',
        TrafficPolicyVersionMarker='string',
        MaxItems='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Specify the value of Id of the traffic policy for which you want to list all versions.
            

    :type TrafficPolicyVersionMarker: string
    :param TrafficPolicyVersionMarker: For your first request to ListTrafficPolicyVersions , do not include the TrafficPolicyVersionMarker parameter.
            If you have more traffic policy versions than the value of MaxItems , ListTrafficPolicyVersions returns only the first group of MaxItems versions. To get the next group of MaxItems traffic policy versions, submit another request to ListTrafficPolicyVersions . For the value of TrafficPolicyVersionMarker , specify the value of the TrafficPolicyVersionMarker element that was returned in the previous response.
            Traffic policy versions are listed in sequential order.
            

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than MaxItems versions, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyVersionMarker element is the ID of the first version in the next group of MaxItems traffic policy versions.

    :rtype: dict
    :return: {
        'TrafficPolicies': [
            {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
                'Document': 'string',
                'Comment': 'string'
            },
        ],
        'IsTruncated': True|False,
        'TrafficPolicyVersionMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Id (string) -- [REQUIRED]
    Specify the value of Id of the traffic policy for which you want to list all versions.
    
    TrafficPolicyVersionMarker (string) -- For your first request to ListTrafficPolicyVersions , do not include the TrafficPolicyVersionMarker parameter.
    If you have more traffic policy versions than the value of MaxItems , ListTrafficPolicyVersions returns only the first group of MaxItems versions. To get the next group of MaxItems traffic policy versions, submit another request to ListTrafficPolicyVersions . For the value of TrafficPolicyVersionMarker , specify the value of the TrafficPolicyVersionMarker element that was returned in the previous response.
    Traffic policy versions are listed in sequential order.
    
    MaxItems (string) -- The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than MaxItems versions, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyVersionMarker element is the ID of the first version in the next group of MaxItems traffic policy versions.
    
    """
    pass

def test_dns_answer(HostedZoneId=None, RecordName=None, RecordType=None, ResolverIP=None, EDNS0ClientSubnetIP=None, EDNS0ClientSubnetMask=None):
    """
    Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask.
    
    
    :example: response = client.test_dns_answer(
        HostedZoneId='string',
        RecordName='string',
        RecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        ResolverIP='string',
        EDNS0ClientSubnetIP='string',
        EDNS0ClientSubnetMask='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
            

    :type RecordName: string
    :param RecordName: [REQUIRED]
            The name of the resource record set that you want Amazon Route 53 to simulate a query for.
            

    :type RecordType: string
    :param RecordType: [REQUIRED]
            The type of the resource record set.
            

    :type ResolverIP: string
    :param ResolverIP: If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, TestDnsAnswer uses the IP address of a DNS resolver in the AWS US East region.

    :type EDNS0ClientSubnetIP: string
    :param EDNS0ClientSubnetIP: If the resolver that you specified for resolverip supports EDNS0, specify the IP address of a client in the applicable location.

    :type EDNS0ClientSubnetMask: string
    :param EDNS0ClientSubnetMask: If you specify an IP address for edns0clientsubnetip , you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify 192.0.2.44 for edns0clientsubnetip and 24 for edns0clientsubnetmask , the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits.

    :rtype: dict
    :return: {
        'Nameserver': 'string',
        'RecordName': 'string',
        'RecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
        'RecordData': [
            'string',
        ],
        'ResponseCode': 'string',
        'Protocol': 'string'
    }
    
    
    :returns: 
    For non-alias resource record sets, a RecordDataEntry element contains one value in the resource record set. If the resource record set contains multiple values, the response includes one RecordDataEntry element for each value.
    For multiple resource record sets that have the same name and type, which includes weighted, latency, geolocation, and failover, a RecordDataEntry element contains the value from the appropriate resource record set based on the request.
    For alias resource record sets that refer to AWS resources other than another resource record set, the RecordDataEntry element contains an IP address or a domain name for the AWS resource, depending on the type of resource.
    For alias resource record sets that refer to other resource record sets, a RecordDataEntry element contains one value from the referenced resource record set. If the referenced resource record set contains multiple values, the response includes one RecordDataEntry element for each value.
    
    """
    pass

def update_health_check(HealthCheckId=None, HealthCheckVersion=None, IPAddress=None, Port=None, ResourcePath=None, FullyQualifiedDomainName=None, SearchString=None, FailureThreshold=None, Inverted=None, HealthThreshold=None, ChildHealthChecks=None, EnableSNI=None, Regions=None, AlarmIdentifier=None, InsufficientDataHealthStatus=None):
    """
    Updates an existing health check.
    Send a POST request to the /2013-04-01/healthcheck/*health check ID* `` resource. The request body must include an XML document with an ``UpdateHealthCheckRequest element. For more information about updating health checks, see Creating, Updating, and Deleting Health Checks in the Amazon Route 53 Developer Guide.
    
    
    :example: response = client.update_health_check(
        HealthCheckId='string',
        HealthCheckVersion=123,
        IPAddress='string',
        Port=123,
        ResourcePath='string',
        FullyQualifiedDomainName='string',
        SearchString='string',
        FailureThreshold=123,
        Inverted=True|False,
        HealthThreshold=123,
        ChildHealthChecks=[
            'string',
        ],
        EnableSNI=True|False,
        Regions=[
            'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
        ],
        AlarmIdentifier={
            'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
            'Name': 'string'
        },
        InsufficientDataHealthStatus='Healthy'|'Unhealthy'|'LastKnownStatus'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]
            The ID for the health check for which you want detailed information. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.
            

    :type HealthCheckVersion: integer
    :param HealthCheckVersion: A sequential counter that Amazon Route 53 sets to 1 when you create a health check and increments by 1 each time you update settings for the health check.
            We recommend that you use GetHealthCheck or ListHealthChecks to get the current value of HealthCheckVersion for the health check that you want to update, and that you include that value in your UpdateHealthCheck request. This prevents Amazon Route 53 from overwriting an intervening update:
            f the value in the UpdateHealthCheck request matches the value of HealthCheckVersion in the health check, Amazon Route 53 updates the health check with the new settings.
            If the value of HealthCheckVersion in the health check is greater, the health check was changed after you got the version number. Amazon Route 53 does not update the health check, and it returns a HealthCheckVersionMismatch error.
            

    :type IPAddress: string
    :param IPAddress: The IPv4 IP address of the endpoint on which you want Amazon Route 53 to perform health checks. If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            f the endpoint is an Amazon EC2 instance, we recommend that you create an Elastic IP address, associate it with your Amazon EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance never changes. For more information, see Elastic IP Addresses (EIP) in the Amazon EC2 User Guide for Linux Instances .
            Note
            If a health check already has a value for IPAddress , you can change the value. However, you can't update an existing health check to add or remove the value of IPAddress .
            For more information, see UpdateHealthCheckRequest$FullyQualifiedDomainName .
            

    :type Port: integer
    :param Port: The port on the endpoint on which you want Amazon Route 53 to perform health checks.

    :type ResourcePath: string
    :param ResourcePath: The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.
            Specify this value only if you want to change it.
            

    :type FullyQualifiedDomainName: string
    :param FullyQualifiedDomainName: Amazon Route 53 behavior depends on whether you specify a value for IPAddress .
            Note
            If a health check already has a value for IPAddress , you can change the value. However, you can't update an existing health check to add or remove the value of IPAddress .
            If you specify IPAddress :
            The value that you want Amazon Route 53 to pass in the Host header in all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Amazon Route 53 to perform health checks. When Amazon Route 53 checks the health of an endpoint, here is how it constructs the Host header:
            If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
            If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Amazon Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
            If you specify another value for Port and any value except TCP for Type , Amazon Route 53 passes * FullyQualifiedDomainName :Port * to the endpoint in the Host header.
            If you don't specify a value for FullyQualifiedDomainName , Amazon Route 53 substitutes the value of IPAddress in the Host header in each of the above cases.
            If you don't specify IPAddress :
            If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to the domain that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-1-www.example.com ), not the name of the resource record sets (www.example.com).
            Warning
            In this configuration, if the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
            In addition, if the value of Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Amazon Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Amazon Route 53 doesn't pass a Host header.
            

    :type SearchString: string
    :param SearchString: If the value of Type is HTTP_STR_MATCH or HTTP_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy. (You can't change the value of Type when you update a health check.)

    :type FailureThreshold: integer
    :param FailureThreshold: The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .

    :type Inverted: boolean
    :param Inverted: Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

    :type HealthThreshold: integer
    :param HealthThreshold: The number of child health checks that are associated with a CALCULATED health that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks and ChildHealthCheck elements.
            Note the following:
            If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy.
            If you specify 0 , Amazon Route 53 always considers this health check to be healthy.
            

    :type ChildHealthChecks: list
    :param ChildHealthChecks: A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.
            (string) --
            

    :type EnableSNI: boolean
    :param EnableSNI: Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
            Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don't enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
            The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.
            

    :type Regions: list
    :param Regions: A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            

    :type AlarmIdentifier: dict
    :param AlarmIdentifier: A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            Region (string) -- [REQUIRED]A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            For the current list of CloudWatch regions, see Amazon CloudWatch in AWS Regions and Endpoints in the Amazon Web Services General Reference .
            Name (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            

    :type InsufficientDataHealthStatus: string
    :param InsufficientDataHealthStatus: When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
            Healthy : Amazon Route 53 considers the health check to be healthy.
            Unhealthy : Amazon Route 53 considers the health check to be unhealthy.
            LastKnownStatus : Amazon Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
            

    :rtype: dict
    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'HealthCheckConfig': {
                'IPAddress': 'string',
                'Port': 123,
                'Type': 'HTTP'|'HTTPS'|'HTTP_STR_MATCH'|'HTTPS_STR_MATCH'|'TCP'|'CALCULATED'|'CLOUDWATCH_METRIC',
                'ResourcePath': 'string',
                'FullyQualifiedDomainName': 'string',
                'SearchString': 'string',
                'RequestInterval': 123,
                'FailureThreshold': 123,
                'MeasureLatency': True|False,
                'Inverted': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
                    'Name': 'string'
                },
                'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
            },
            'HealthCheckVersion': 123,
            'CloudWatchAlarmConfiguration': {
                'EvaluationPeriods': 123,
                'Threshold': 123.0,
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'Period': 123,
                'MetricName': 'string',
                'Namespace': 'string',
                'Statistic': 'Average'|'Sum'|'SampleCount'|'Maximum'|'Minimum',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    HTTP : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Amazon Route 53 tries to establish a TCP connection. If successful, Amazon Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    """
    pass

def update_hosted_zone_comment(Id=None, Comment=None):
    """
    Updates the hosted zone comment. Send a POST request to the ``/2013-04-01/hostedzone/hosted zone ID `` resource.
    
    
    :example: response = client.update_hosted_zone_comment(
        Id='string',
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID for the hosted zone for which you want to update the comment.
            

    :type Comment: string
    :param Comment: The new comment for the hosted zone. If you don't specify a value for Comment , Amazon Route 53 deletes the existing value of the Comment element, if any.

    :rtype: dict
    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123
        }
    }
    
    
    """
    pass

def update_traffic_policy_comment(Id=None, Version=None, Comment=None):
    """
    Updates the comment for a specified traffic policy version.
    Send a POST request to the /2013-04-01/trafficpolicy/ resource.
    The request body must include a document with an UpdateTrafficPolicyCommentRequest element.
    
    
    :example: response = client.update_traffic_policy_comment(
        Id='string',
        Version=123,
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The value of Id for the traffic policy for which you want to update the comment.
            

    :type Version: integer
    :param Version: [REQUIRED]
            The value of Version for the traffic policy for which you want to update the comment.
            

    :type Comment: string
    :param Comment: [REQUIRED]
            The new comment for the specified traffic policy and version.
            

    :rtype: dict
    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA',
            'Document': 'string',
            'Comment': 'string'
        }
    }
    
    
    """
    pass

def update_traffic_policy_instance(Id=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
    """
    Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.
    Send a POST request to the /2013-04-01/trafficpolicyinstance/*traffic policy ID* `` resource. The request body must include a document with an ``UpdateTrafficPolicyInstanceRequest element.
    When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Amazon Route 53 performs the following operations:
    
    
    :example: response = client.update_traffic_policy_instance(
        Id='string',
        TTL=123,
        TrafficPolicyId='string',
        TrafficPolicyVersion=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to update.
            

    :type TTL: integer
    :param TTL: [REQUIRED]
            The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.
            

    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
            

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
            

    :rtype: dict
    :return: {
        'TrafficPolicyInstance': {
            'Id': 'string',
            'HostedZoneId': 'string',
            'Name': 'string',
            'TTL': 123,
            'State': 'string',
            'Message': 'string',
            'TrafficPolicyId': 'string',
            'TrafficPolicyVersion': 123,
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
        }
    }
    
    
    :returns: 
    Id (string) -- [REQUIRED]
    The ID of the traffic policy instance that you want to update.
    
    TTL (integer) -- [REQUIRED]
    The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.
    
    TrafficPolicyId (string) -- [REQUIRED]
    The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
    
    TrafficPolicyVersion (integer) -- [REQUIRED]
    The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
    
    
    """
    pass

