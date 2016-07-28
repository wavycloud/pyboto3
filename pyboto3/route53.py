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


class Route53(object):
    def __init__(self):
        self.client = boto3.client('Route53')

    def associate_vpc_with_hosted_zone(self, HostedZoneId=None, VPC=None, Comment=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone you want to associate your VPC with.
            Note that you cannot associate a VPC with a hosted zone that doesn't have an existing VPC association.
            
        :type HostedZoneId: string
        :param VPC: [REQUIRED]
            The VPC that you want your hosted zone to be associated with.
            VPCRegion (string) --
            VPCId (string) --A VPC ID
            
        :type VPC: dict
        :param Comment: Optional: Any comments you want to include about a AssociateVPCWithHostedZoneRequest .
        :type Comment: string
        """
        self.client.associate_vpc_with_hosted_zone(HostedZoneId=HostedZoneId, VPC=VPC, Comment=Comment)

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

    def change_resource_record_sets(self, HostedZoneId=None, ChangeBatch=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to change.
            
        :type HostedZoneId: string
        :param ChangeBatch: [REQUIRED]
            A complex type that contains an optional comment and the Changes element.
            Comment (string) --Optional: Any comments you want to include about a change batch request.
            Changes (list) -- [REQUIRED]A complex type that contains one Change element for each resource record set that you want to create or delete.
            (dict) --A complex type that contains the information for each change in a change batch request.
            Action (string) -- [REQUIRED]The action to perform:
            CREATE : Creates a resource record set that has the specified values.
            DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
            UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
            ResourceRecordSet (dict) -- [REQUIRED]Information about the resource record set to create or delete.
            Name (string) -- [REQUIRED]The name of the domain you want to perform the action on.
            Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            For information about how to specify characters other than a-z, 0-9, and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
            You can use an asterisk (*) character in the name. DNS treats the * character either as a wildcard or as the * character (ASCII 42), depending on where it appears in the name. For more information, see Using an Asterisk (*) in the Names of Hosted Zones and Resource Record Sets in the Amazon Route 53 Developer Guide
            Warning
            You can't use the * wildcard for resource records sets that have a type of NS.
            Type (string) -- [REQUIRED]The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            Valid values for basic resource record sets: A | AAAA | CNAME | MX | NS | PTR | SOA | SPF | SRV | TXT
            Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CNAME | MX | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
            Note
            SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, '...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.' In RFC 7208, see section 14.1, The SPF DNS Record Type .
            Values for alias resource record sets:
            CloudFront distributions: A
            ELB load balancers: A | AAAA
            Amazon S3 buckets: A
            Another resource record set in this hosted zone: Specify the type of the resource record set for which you're creating the alias. Specify any value except NS or SOA .
            SetIdentifier (string) --Weighted, Latency, Geo, and Failover resource record sets only: An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of SetIdentifier must be unique for each resource record set that has the same combination of DNS name and type.
            Weight (integer) --Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:
            You must specify a value for the Weight element for every weighted resource record set.
            You can only specify one ResourceRecord per weighted resource record set.
            You cannot create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
            You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
            For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .
            Region (string) --Latency-based resource record sets only: The Amazon EC2 region where the resource that is specified in this resource record set resides. The resource typically is an AWS resource, such as an Amazon EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
            Note
            You can create latency and latency alias resource record sets only in public hosted zones.
            When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 region. Amazon Route 53 then returns the value that is associated with the selected resource record set.
            Note the following:
            You can only specify one ResourceRecord per latency resource record set.
            You can only create one latency resource record set for each Amazon EC2 region.
            You are not required to create latency resource record sets for all Amazon EC2 regions. Amazon Route 53 will choose the region with the best latency from among the regions for which you create latency resource record sets.
            You cannot create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.
            GeoLocation (dict) --Geo location resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .
            Note
            You can create geolocation and geolocation alias resource record sets only in public hosted zones.
            If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
            You cannot create two geolocation resource record sets that specify the same geographic location.
            The value * in the CountryCode element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the Name and Type elements.
            Warning
            Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of CountryCode is * , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a * resource record set, Amazon Route 53 returns a 'no answer' response for queries from those locations.
            You cannot create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.
            ContinentCode (string) --The code for a continent geo location. Note: only continent locations have a continent code.
            Valid values: AF | AN | AS | EU | OC | NA | SA
            Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
            CountryCode (string) --The code for a country geo location. The default location uses '*' for the country code and will match all locations that are not matched by a geo location.
            The default geo location uses a * for the country code. All other country codes follow the ISO 3166 two-character code.
            SubdivisionCode (string) --The code for a country's subdivision (e.g., a province of Canada). A subdivision code is only valid with the appropriate country code.
            Constraint: Specifying SubdivisionCode without CountryCode returns an InvalidInput error.
            Failover (string) --Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
            Note
            You can create failover and failover alias resource record sets only in public hosted zones.
            Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:
            When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
            When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
            When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
            If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.
            You cannot create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
            For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
            For more information about configuring failover for Amazon Route 53, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
            Valid values: PRIMARY | SECONDARY
            TTL (integer) --The cache time to live for the current resource record set. Note the following:
            If you're creating a non-alias resource record set, TTL is required.
            If you're creating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
            If you're associating this resource record set with a health check (if you're adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
            All of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets must have the same value for TTL .
            If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .
            ResourceRecords (list) --A complex type that contains the resource records for the current resource record set.
            (dict) --A complex type that contains the value of the Value element for the current resource record set.
            Value (string) -- [REQUIRED]The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            You can specify more than one value for all record types except CNAME and SOA .
            
            AliasTarget (dict) --Alias resource record sets only: Information about the AWS resource to which you are redirecting traffic.
            HostedZoneId (string) -- [REQUIRED]Alias resource record sets only: The value you use depends on where you want to route queries:
            A CloudFront distribution: Specify Z2FDTNDATAQYW2 .
            An ELB load balancer: Specify the value of the hosted zone ID for the load balancer. You can get the hosted zone ID by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
            An Amazon S3 bucket that is configured as a static website: Specify the hosted zone ID for the Amazon S3 website endpoint in which you created the bucket. For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference .
            Another Amazon Route 53 resource record set in your hosted zone: Specify the hosted zone ID of your hosted zone. (An alias resource record set cannot reference a resource record set in a different hosted zone.)
            DNSName (string) -- [REQUIRED]Alias resource record sets only: The external DNS name associated with the AWS Resource. The value that you specify depends on where you want to route queries:
            A CloudFront distribution: Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
            An ELB load balancer: Specify the DNS name associated with the load balancer. You can get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
            An Elastic Beanstalk environment: Specify the CNAME attribute for the environment. (The environment must have a regionalized domain name.)
            An Amazon S3 bucket that is configured as a static website: Specify the domain name of the Amazon S3 website endpoint in which you created the bucket; for example, s3-website-us-east-1.amazonaws.com . For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference . For more information about using Amazon S3 buckets for websites, see Hosting a Static Website on Amazon S3 in the Amazon Simple Storage Service Developer Guide .
            Another Amazon Route 53 resource record set: Specify the value of the Name element for a resource record set in the current hosted zone.
            EvaluateTargetHealth (boolean) -- [REQUIRED]Alias resource record sets only: If you set the value of EvaluateTargetHealth to true for the resource record set or sets in an alias, weighted alias, latency alias, or failover alias resource record set, and if you specify a value for HealthCheckId for every resource record set that is referenced by these alias resource record sets, the alias resource record sets inherit the health of the referenced resource record sets.
            In this configuration, when Amazon Route 53 receives a DNS query for an alias resource record set:
            Amazon Route 53 looks at the resource record sets that are referenced by the alias resource record sets to determine which health checks they're using.
            Amazon Route 53 checks the current status of each health check. (Amazon Route 53 periodically checks the health of the endpoint that is specified in a health check; it doesn't perform the health check when the DNS query arrives.)
            Based on the status of the health checks, Amazon Route 53 determines which resource record sets are healthy. Unhealthy resource record sets are immediately removed from consideration. In addition, if all of the resource record sets that are referenced by an alias resource record set are unhealthy, that alias resource record set also is immediately removed from consideration.
            Based on the configuration of the alias resource record sets (weighted alias or latency alias, for example) and the configuration of the resource record sets that they reference, Amazon Route 53 chooses a resource record set from the healthy resource record sets, and responds to the query.
            Note the following:
            You cannot set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.
            If the AWS resource that you specify in AliasTarget is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target.
            If you specify an ELB load balancer in AliasTarget , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If no Amazon EC2 instances are healthy or if the load balancer itself is unhealthy, and if EvaluateTargetHealth is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources.
            When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the Amazon EC2 instances that you register with an ELB load balancer. For more information, see How Health Checks Work in More Complex Amazon Route 53 Configurations in the Amazon Route 53 Developer Guide .
            We recommend that you set EvaluateTargetHealth to true only when you have enough idle capacity to handle the failure of one or more endpoints.
            For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
            HealthCheckId (string) --Health Check resource record sets only, not required for alias resource record sets: An identifier that is used to identify health check associated with the resource record set.
            TrafficPolicyInstanceId (string) --
            
            
        :type ChangeBatch: dict
        """
        self.client.change_resource_record_sets(HostedZoneId=HostedZoneId, ChangeBatch=ChangeBatch)

    def change_tags_for_resource(self, ResourceType=None, ResourceId=None, AddTags=None, RemoveTagKeys=None):
        """
        :param ResourceType: [REQUIRED]
            The type of the resource.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            
        :type ResourceType: string
        :param ResourceId: [REQUIRED]
            The ID of the resource for which you want to add, change, or delete tags.
            
        :type ResourceId: string
        :param AddTags: A complex type that contains a list of Tag elements. Each Tag element identifies a tag that you want to add or update for the specified resource.
            (dict) --A single tag containing a key and value.
            Key (string) --The key for a Tag .
            Value (string) --The value for a Tag .
            
            
        :type AddTags: list
        :param RemoveTagKeys: A list of Tag keys that you want to remove from the specified resource.
            (string) --
            
        :type RemoveTagKeys: list
        """
        self.client.change_tags_for_resource(ResourceType=ResourceType, ResourceId=ResourceId, AddTags=AddTags,
                                             RemoveTagKeys=RemoveTagKeys)

    def create_health_check(self, CallerReference=None, HealthCheckConfig=None):
        """
        :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHealthCheck requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a health check. CallerReference can be any unique string; you might choose to use a string that identifies your project.
            Valid characters are any Unicode code points that are legal in an XML 1.0 document. The UTF-8 encoding of the value must be less than 128 bytes.
            
        :type CallerReference: string
        :param HealthCheckConfig: [REQUIRED]
            A complex type that contains health check configuration.
            IPAddress (string) --IP Address of the instance being checked.
            Port (integer) --Port on which connection will be opened to the instance to health check. For HTTP and HTTP_STR_MATCH this defaults to 80 if the port is not specified. For HTTPS and HTTPS_STR_MATCH this defaults to 443 if the port is not specified.
            Type (string) -- [REQUIRED]The type of health check to be performed. Currently supported types are TCP, HTTP, HTTPS, HTTP_STR_MATCH, HTTPS_STR_MATCH, CALCULATED and CLOUDWATCH_METRIC.
            ResourcePath (string) --Path to ping on the instance to check the health. Required for HTTP, HTTPS, HTTP_STR_MATCH, and HTTPS_STR_MATCH health checks. The HTTP request is issued to the instance on the given port and path.
            FullyQualifiedDomainName (string) --Fully qualified domain name of the instance to be health checked.
            SearchString (string) --A string to search for in the body of a health check response. Required for HTTP_STR_MATCH and HTTPS_STR_MATCH health checks. Amazon Route 53 considers case when searching for SearchString in the response body.
            RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
            Each Amazon Route 53 health checker makes requests at this interval. Valid values are 10 and 30. The default value is 30.
            FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.
            Valid values are integers between 1 and 10. For more information, see 'How Amazon Route 53 Determines Whether an Endpoint Is Healthy' in the Amazon Route 53 Developer Guide.
            MeasureLatency (boolean) --A Boolean value that indicates whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Amazon Route 53 console.
            Inverted (boolean) --A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Amazon Route 53 considers the health check to be unhealthy.
            HealthThreshold (integer) --The minimum number of child health checks that must be healthy for Amazon Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive.
            ChildHealthChecks (list) --For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
            (string) --
            EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. If you don't specify a value for EnableSNI , Amazon Route 53 defaults to true when Type is HTTPS or HTTPS_STR_MATCH and defaults to false when Type is any other value.
            Regions (list) --A list of HealthCheckRegion values that you want Amazon Route 53 to use to perform health checks for the specified endpoint. You must specify at least three regions.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            AlarmIdentifier (dict) --A complex type that contains information to uniquely identify the CloudWatch alarm that you're associating with a Route 53 health check.
            Region (string) -- [REQUIRED]The CloudWatchRegion that the CloudWatch alarm was created in.
            Name (string) -- [REQUIRED]The name of the CloudWatch alarm.
            InsufficientDataHealthStatus (string) --The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are Healthy , Unhealthy and LastKnownStatus .
            
        :type HealthCheckConfig: dict
        """
        self.client.create_health_check(CallerReference=CallerReference, HealthCheckConfig=HealthCheckConfig)

    def create_hosted_zone(self, Name=None, VPC=None, CallerReference=None, HostedZoneConfig=None,
                           DelegationSetId=None):
        """
        :param Name: [REQUIRED]
            The name of the domain. This must be a fully-specified domain, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            This is the name you have registered with your DNS registrar. You should ask your registrar to change the authoritative name servers for your domain to the set of NameServers elements returned in DelegationSet .
            
        :type Name: string
        :param VPC: The VPC that you want your hosted zone to be associated with. By providing this parameter, your newly created hosted cannot be resolved anywhere other than the given VPC.
            VPCRegion (string) --
            VPCId (string) --A VPC ID
            
        :type VPC: dict
        :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a hosted zone. CallerReference can be any unique string; you might choose to use a string that identifies your project, such as DNSMigration_01 .
            Valid characters are any Unicode code points that are legal in an XML 1.0 document. The UTF-8 encoding of the value must be less than 128 bytes.
            
        :type CallerReference: string
        :param HostedZoneConfig: A complex type that contains an optional comment about your hosted zone.
            Comment (string) --An optional comment about your hosted zone. If you don't want to specify a comment, you can omit the HostedZoneConfig and Comment elements from the XML document.
            PrivateZone (boolean) --GetHostedZone and ListHostedZone responses: A Boolean value that indicates whether a hosted zone is private.
            CreateHostedZone requests: When you're creating a private hosted zone (when you specify values for VPCId and VPCRegion), you can optionally specify true for PrivateZone.
            
        :type HostedZoneConfig: dict
        :param DelegationSetId: The delegation set id of the reusable delgation set whose NS records you want to assign to the new hosted zone.
        :type DelegationSetId: string
        """
        self.client.create_hosted_zone(Name=Name, VPC=VPC, CallerReference=CallerReference,
                                       HostedZoneConfig=HostedZoneConfig, DelegationSetId=DelegationSetId)

    def create_reusable_delegation_set(self, CallerReference=None, HostedZoneId=None):
        """
        :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateReusableDelegationSet requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a reusable delegation set. CallerReference can be any unique string; you might choose to use a string that identifies your project, such as DNSMigration_01 .
            Valid characters are any Unicode code points that are legal in an XML 1.0 document. The UTF-8 encoding of the value must be less than 128 bytes.
            
        :type CallerReference: string
        :param HostedZoneId: The ID of the hosted zone whose delegation set you want to mark as reusable. It is an optional parameter.
        :type HostedZoneId: string
        """
        self.client.create_reusable_delegation_set(CallerReference=CallerReference, HostedZoneId=HostedZoneId)

    def create_traffic_policy(self, Name=None, Document=None, Comment=None):
        """
        :param Name: [REQUIRED]
            The name of the traffic policy.
            
        :type Name: string
        :param Document: [REQUIRED]
            The definition of this traffic policy in JSON format. For more information, see Traffic Policy Document Format in the Amazon Route 53 API Reference .
            
        :type Document: string
        :param Comment: Any comments that you want to include about the traffic policy.
        :type Comment: string
        """
        self.client.create_traffic_policy(Name=Name, Document=Document, Comment=Comment)

    def create_traffic_policy_instance(self, HostedZoneId=None, Name=None, TTL=None, TrafficPolicyId=None,
                                       TrafficPolicyVersion=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone in which you want Amazon Route 53 to create resource record sets by using the configuration in a traffic policy.
            
        :type HostedZoneId: string
        :param Name: [REQUIRED]
            The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Amazon Route 53 creates for this traffic policy instance.
            
        :type Name: string
        :param TTL: [REQUIRED]
            The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.
            
        :type TTL: integer
        :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            
        :type TrafficPolicyId: string
        :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            
        :type TrafficPolicyVersion: integer
        """
        self.client.create_traffic_policy_instance(HostedZoneId=HostedZoneId, Name=Name, TTL=TTL,
                                                   TrafficPolicyId=TrafficPolicyId,
                                                   TrafficPolicyVersion=TrafficPolicyVersion)

    def create_traffic_policy_version(self, Id=None, Document=None, Comment=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy for which you want to create a new version.
            
        :type Id: string
        :param Document: [REQUIRED]
            The definition of a new traffic policy version, in JSON format. You must specify the full definition of the new traffic policy. You cannot specify just the differences between the new version and a previous version. For more information, see Traffic Policy Document Format in the Amazon Route 53 API Reference .
            
        :type Document: string
        :param Comment: Any comments that you want to include about the new traffic policy version.
        :type Comment: string
        """
        self.client.create_traffic_policy_version(Id=Id, Document=Document, Comment=Comment)

    def delete_health_check(self, HealthCheckId=None):
        """
        :param HealthCheckId: [REQUIRED]
            The ID of the health check to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Empty response for the request.
            
            
        :type HealthCheckId: string
        """
        self.client.delete_health_check(HealthCheckId=HealthCheckId)

    def delete_hosted_zone(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the hosted zone you want to delete.
            Return typedict
            ReturnsResponse Syntax{
              'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
              }
            }
            Response Structure
            (dict) --A complex type containing the response information for the request.
            ChangeInfo (dict) --A complex type that contains the ID, the status, and the date and time of your delete request.
            Id (string) --The ID of the request. Use this ID to track when the change has completed across all Amazon Route 53 DNS servers.
            Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
            Valid Values: PENDING | INSYNC
            SubmittedAt (datetime) --The date and time the change was submitted, in the format YYYY-MM-DDThh:mm:ssZ , as specified in the ISO 8601 standard (for example, 2009-11-19T19:37:58Z). The Z after the time indicates that the time is listed in Coordinated Universal Time (UTC).
            Comment (string) --A complex type that describes change information about changes made to your hosted zone.
            This element contains an ID that you use when performing a GetChange action to get detailed information about the change.
            
            
            
        :type Id: string
        """
        self.client.delete_hosted_zone(Id=Id)

    def delete_reusable_delegation_set(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the reusable delegation set you want to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Empty response for the request.
            
            
        :type Id: string
        """
        self.client.delete_reusable_delegation_set(Id=Id)

    def delete_traffic_policy(self, Id=None, Version=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy that you want to delete.
            
        :type Id: string
        :param Version: [REQUIRED]
            The version number of the traffic policy that you want to delete.
            
        :type Version: integer
        """
        self.client.delete_traffic_policy(Id=Id, Version=Version)

    def delete_traffic_policy_instance(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to delete.
            Warning
            When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element.
            
            
        :type Id: string
        """
        self.client.delete_traffic_policy_instance(Id=Id)

    def disassociate_vpc_from_hosted_zone(self, HostedZoneId=None, VPC=None, Comment=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone you want to disassociate your VPC from.
            Note that you cannot disassociate the last VPC from a hosted zone.
            
        :type HostedZoneId: string
        :param VPC: [REQUIRED]
            The VPC that you want your hosted zone to be disassociated from.
            VPCRegion (string) --
            VPCId (string) --A VPC ID
            
        :type VPC: dict
        :param Comment: Optional: Any comments you want to include about a DisassociateVPCFromHostedZoneRequest .
        :type Comment: string
        """
        self.client.disassociate_vpc_from_hosted_zone(HostedZoneId=HostedZoneId, VPC=VPC, Comment=Comment)

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

    def get_change(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the change batch request. The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.
            Return typedict
            ReturnsResponse Syntax{
              'ChangeInfo': {
                'Id': 'string',
                'Status': 'PENDING'|'INSYNC',
                'SubmittedAt': datetime(2015, 1, 1),
                'Comment': 'string'
              }
            }
            Response Structure
            (dict) --A complex type that contains the ChangeInfo element.
            ChangeInfo (dict) --A complex type that contains information about the specified change batch, including the change batch ID, the status of the change, and the date and time of the request.
            Id (string) --The ID of the request. Use this ID to track when the change has completed across all Amazon Route 53 DNS servers.
            Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
            Valid Values: PENDING | INSYNC
            SubmittedAt (datetime) --The date and time the change was submitted, in the format YYYY-MM-DDThh:mm:ssZ , as specified in the ISO 8601 standard (for example, 2009-11-19T19:37:58Z). The Z after the time indicates that the time is listed in Coordinated Universal Time (UTC).
            Comment (string) --A complex type that describes change information about changes made to your hosted zone.
            This element contains an ID that you use when performing a GetChange action to get detailed information about the change.
            
            
            
        :type Id: string
        """
        self.client.get_change(Id=Id)

    def get_change_details(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the change batch request. The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.
            Return typedict
            ReturnsResponse Syntax{
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
                      'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'PTR'|'SRV'|'SPF'|'AAAA',
                      'SetIdentifier': 'string',
                      'Weight': 123,
                      'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1'|'ap-south-1',
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
            Response Structure
            (dict) --A complex type that contains the ChangeBatchRecord element.
            ChangeBatchRecord (dict) --A complex type that contains information about the specified change batch, including the change batch ID, the status of the change, and the contained changes.
            Id (string) --The ID of the request. Use this ID to track when the change has completed across all Amazon Route 53 DNS servers.
            SubmittedAt (datetime) --The date and time the change was submitted, in the format YYYY-MM-DDThh:mm:ssZ , as specified in the ISO 8601 standard (for example, 2009-11-19T19:37:58Z). The Z after the time indicates that the time is listed in Coordinated Universal Time (UTC).
            Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
            Valid Values: PENDING | INSYNC
            Comment (string) --A complex type that describes change information about changes made to your hosted zone.
            This element contains an ID that you use when performing a GetChange action to get detailed information about the change.
            Submitter (string) --The AWS account ID attached to the changes.
            Changes (list) --A list of changes made in the ChangeBatch.
            (dict) --A complex type that contains the information for each change in a change batch request.
            Action (string) --The action to perform:
            CREATE : Creates a resource record set that has the specified values.
            DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
            UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
            ResourceRecordSet (dict) --Information about the resource record set to create or delete.
            Name (string) --The name of the domain you want to perform the action on.
            Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            For information about how to specify characters other than a-z, 0-9, and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
            You can use an asterisk (*) character in the name. DNS treats the * character either as a wildcard or as the * character (ASCII 42), depending on where it appears in the name. For more information, see Using an Asterisk (*) in the Names of Hosted Zones and Resource Record Sets in the Amazon Route 53 Developer Guide
            Warning
            You can't use the * wildcard for resource records sets that have a type of NS.
            Type (string) --The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            Valid values for basic resource record sets: A | AAAA | CNAME | MX | NS | PTR | SOA | SPF | SRV | TXT
            Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CNAME | MX | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
            Note
            SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, '...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.' In RFC 7208, see section 14.1, The SPF DNS Record Type .
            Values for alias resource record sets:
            CloudFront distributions: A
            ELB load balancers: A | AAAA
            Amazon S3 buckets: A
            Another resource record set in this hosted zone: Specify the type of the resource record set for which you're creating the alias. Specify any value except NS or SOA .
            SetIdentifier (string) --Weighted, Latency, Geo, and Failover resource record sets only: An identifier that differentiates among multiple resource record sets that have the same combination of DNS name and type. The value of SetIdentifier must be unique for each resource record set that has the same combination of DNS name and type.
            Weight (integer) --Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Amazon Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Amazon Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:
            You must specify a value for the Weight element for every weighted resource record set.
            You can only specify one ResourceRecord per weighted resource record set.
            You cannot create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
            You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
            For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Amazon Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Amazon Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .
            Region (string) --Latency-based resource record sets only: The Amazon EC2 region where the resource that is specified in this resource record set resides. The resource typically is an AWS resource, such as an Amazon EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
            Note
            You can create latency and latency alias resource record sets only in public hosted zones.
            When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Amazon Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 region. Amazon Route 53 then returns the value that is associated with the selected resource record set.
            Note the following:
            You can only specify one ResourceRecord per latency resource record set.
            You can only create one latency resource record set for each Amazon EC2 region.
            You are not required to create latency resource record sets for all Amazon EC2 regions. Amazon Route 53 will choose the region with the best latency from among the regions for which you create latency resource record sets.
            You cannot create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.
            GeoLocation (dict) --Geo location resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .
            Note
            You can create geolocation and geolocation alias resource record sets only in public hosted zones.
            If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
            You cannot create two geolocation resource record sets that specify the same geographic location.
            The value * in the CountryCode element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the Name and Type elements.
            Warning
            Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Amazon Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of CountryCode is * , which handles both queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a * resource record set, Amazon Route 53 returns a 'no answer' response for queries from those locations.
            You cannot create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.
            ContinentCode (string) --The code for a continent geo location. Note: only continent locations have a continent code.
            Valid values: AF | AN | AS | EU | OC | NA | SA
            Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
            CountryCode (string) --The code for a country geo location. The default location uses '*' for the country code and will match all locations that are not matched by a geo location.
            The default geo location uses a * for the country code. All other country codes follow the ISO 3166 two-character code.
            SubdivisionCode (string) --The code for a country's subdivision (e.g., a province of Canada). A subdivision code is only valid with the appropriate country code.
            Constraint: Specifying SubdivisionCode without CountryCode returns an InvalidInput error.
            Failover (string) --Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
            Note
            You can create failover and failover alias resource record sets only in public hosted zones.
            Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:
            When the primary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
            When the primary resource record set is unhealthy and the secondary resource record set is healthy, Amazon Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
            When the secondary resource record set is unhealthy, Amazon Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
            If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Amazon Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.
            You cannot create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
            For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
            For more information about configuring failover for Amazon Route 53, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
            Valid values: PRIMARY | SECONDARY
            TTL (integer) --The cache time to live for the current resource record set. Note the following:
            If you're creating a non-alias resource record set, TTL is required.
            If you're creating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
            If you're associating this resource record set with a health check (if you're adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
            All of the resource record sets in a group of weighted, latency, geolocation, or failover resource record sets must have the same value for TTL .
            If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .
            ResourceRecords (list) --A complex type that contains the resource records for the current resource record set.
            (dict) --A complex type that contains the value of the Value element for the current resource record set.
            Value (string) --The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            You can specify more than one value for all record types except CNAME and SOA .
            
            AliasTarget (dict) --Alias resource record sets only: Information about the AWS resource to which you are redirecting traffic.
            HostedZoneId (string) --Alias resource record sets only: The value you use depends on where you want to route queries:
            A CloudFront distribution: Specify Z2FDTNDATAQYW2 .
            An ELB load balancer: Specify the value of the hosted zone ID for the load balancer. You can get the hosted zone ID by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
            An Amazon S3 bucket that is configured as a static website: Specify the hosted zone ID for the Amazon S3 website endpoint in which you created the bucket. For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference .
            Another Amazon Route 53 resource record set in your hosted zone: Specify the hosted zone ID of your hosted zone. (An alias resource record set cannot reference a resource record set in a different hosted zone.)
            DNSName (string) --Alias resource record sets only: The external DNS name associated with the AWS Resource. The value that you specify depends on where you want to route queries:
            A CloudFront distribution: Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
            An ELB load balancer: Specify the DNS name associated with the load balancer. You can get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. Use the same method to get values for HostedZoneId and DNSName . If you get one value from the console and the other value from the API or the CLI, creating the resource record set will fail.
            An Elastic Beanstalk environment: Specify the CNAME attribute for the environment. (The environment must have a regionalized domain name.)
            An Amazon S3 bucket that is configured as a static website: Specify the domain name of the Amazon S3 website endpoint in which you created the bucket; for example, s3-website-us-east-1.amazonaws.com . For more information about valid values, see the table Amazon Simple Storage Service (S3) Website Endpoints in the Amazon Web Services General Reference . For more information about using Amazon S3 buckets for websites, see Hosting a Static Website on Amazon S3 in the Amazon Simple Storage Service Developer Guide .
            Another Amazon Route 53 resource record set: Specify the value of the Name element for a resource record set in the current hosted zone.
            EvaluateTargetHealth (boolean) --Alias resource record sets only: If you set the value of EvaluateTargetHealth to true for the resource record set or sets in an alias, weighted alias, latency alias, or failover alias resource record set, and if you specify a value for HealthCheckId for every resource record set that is referenced by these alias resource record sets, the alias resource record sets inherit the health of the referenced resource record sets.
            In this configuration, when Amazon Route 53 receives a DNS query for an alias resource record set:
            Amazon Route 53 looks at the resource record sets that are referenced by the alias resource record sets to determine which health checks they're using.
            Amazon Route 53 checks the current status of each health check. (Amazon Route 53 periodically checks the health of the endpoint that is specified in a health check; it doesn't perform the health check when the DNS query arrives.)
            Based on the status of the health checks, Amazon Route 53 determines which resource record sets are healthy. Unhealthy resource record sets are immediately removed from consideration. In addition, if all of the resource record sets that are referenced by an alias resource record set are unhealthy, that alias resource record set also is immediately removed from consideration.
            Based on the configuration of the alias resource record sets (weighted alias or latency alias, for example) and the configuration of the resource record sets that they reference, Amazon Route 53 chooses a resource record set from the healthy resource record sets, and responds to the query.
            Note the following:
            You cannot set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.
            If the AWS resource that you specify in AliasTarget is a resource record set or a group of resource record sets (for example, a group of weighted resource record sets), but it is not another alias resource record set, we recommend that you associate a health check with all of the resource record sets in the alias target.
            If you specify an ELB load balancer in AliasTarget , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If no Amazon EC2 instances are healthy or if the load balancer itself is unhealthy, and if EvaluateTargetHealth is true for the corresponding alias resource record set, Amazon Route 53 routes queries to other resources.
            When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Amazon Route 53 health checks, but they perform a similar function. Do not create Amazon Route 53 health checks for the Amazon EC2 instances that you register with an ELB load balancer. For more information, see How Health Checks Work in More Complex Amazon Route 53 Configurations in the Amazon Route 53 Developer Guide .
            We recommend that you set EvaluateTargetHealth to true only when you have enough idle capacity to handle the failure of one or more endpoints.
            For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
            HealthCheckId (string) --Health Check resource record sets only, not required for alias resource record sets: An identifier that is used to identify health check associated with the resource record set.
            TrafficPolicyInstanceId (string) --
            
            
            
            
        :type Id: string
        """
        self.client.get_change_details(Id=Id)

    def get_checker_ip_ranges(self):
        """
        """
        self.client.get_checker_ip_ranges()

    def get_geo_location(self, ContinentCode=None, CountryCode=None, SubdivisionCode=None):
        """
        :param ContinentCode: The code for a continent geo location. Note: only continent locations have a continent code.
            Valid values: AF | AN | AS | EU | OC | NA | SA
            Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
            
        :type ContinentCode: string
        :param CountryCode: The code for a country geo location. The default location uses '*' for the country code and will match all locations that are not matched by a geo location.
            The default geo location uses a * for the country code. All other country codes follow the ISO 3166 two-character code.
            
        :type CountryCode: string
        :param SubdivisionCode: The code for a country's subdivision (e.g., a province of Canada). A subdivision code is only valid with the appropriate country code.
            Constraint: Specifying SubdivisionCode without CountryCode returns an InvalidInput error.
            
        :type SubdivisionCode: string
        """
        self.client.get_geo_location(ContinentCode=ContinentCode, CountryCode=CountryCode,
                                     SubdivisionCode=SubdivisionCode)

    def get_health_check(self, HealthCheckId=None):
        """
        :param HealthCheckId: [REQUIRED]
            The ID of the health check to retrieve.
            Return typedict
            ReturnsResponse Syntax{
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
                    'Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1',
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
            Response Structure
            (dict) --A complex type containing information about the specified health check.
            HealthCheck (dict) --A complex type that contains the information about the specified health check.
            Id (string) --The ID of the specified health check.
            CallerReference (string) --A unique string that identifies the request to create the health check.
            HealthCheckConfig (dict) --A complex type that contains the health check configuration.
            IPAddress (string) --IP Address of the instance being checked.
            Port (integer) --Port on which connection will be opened to the instance to health check. For HTTP and HTTP_STR_MATCH this defaults to 80 if the port is not specified. For HTTPS and HTTPS_STR_MATCH this defaults to 443 if the port is not specified.
            Type (string) --The type of health check to be performed. Currently supported types are TCP, HTTP, HTTPS, HTTP_STR_MATCH, HTTPS_STR_MATCH, CALCULATED and CLOUDWATCH_METRIC.
            ResourcePath (string) --Path to ping on the instance to check the health. Required for HTTP, HTTPS, HTTP_STR_MATCH, and HTTPS_STR_MATCH health checks. The HTTP request is issued to the instance on the given port and path.
            FullyQualifiedDomainName (string) --Fully qualified domain name of the instance to be health checked.
            SearchString (string) --A string to search for in the body of a health check response. Required for HTTP_STR_MATCH and HTTPS_STR_MATCH health checks. Amazon Route 53 considers case when searching for SearchString in the response body.
            RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
            Each Amazon Route 53 health checker makes requests at this interval. Valid values are 10 and 30. The default value is 30.
            FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.
            Valid values are integers between 1 and 10. For more information, see 'How Amazon Route 53 Determines Whether an Endpoint Is Healthy' in the Amazon Route 53 Developer Guide.
            MeasureLatency (boolean) --A Boolean value that indicates whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Amazon Route 53 console.
            Inverted (boolean) --A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Amazon Route 53 considers the health check to be unhealthy.
            HealthThreshold (integer) --The minimum number of child health checks that must be healthy for Amazon Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive.
            ChildHealthChecks (list) --For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
            (string) --
            EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. If you don't specify a value for EnableSNI , Amazon Route 53 defaults to true when Type is HTTPS or HTTPS_STR_MATCH and defaults to false when Type is any other value.
            Regions (list) --A list of HealthCheckRegion values that you want Amazon Route 53 to use to perform health checks for the specified endpoint. You must specify at least three regions.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            AlarmIdentifier (dict) --A complex type that contains information to uniquely identify the CloudWatch alarm that you're associating with a Route 53 health check.
            Region (string) --The CloudWatchRegion that the CloudWatch alarm was created in.
            Name (string) --The name of the CloudWatch alarm.
            InsufficientDataHealthStatus (string) --The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are Healthy , Unhealthy and LastKnownStatus .
            HealthCheckVersion (integer) --The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.
            CloudWatchAlarmConfiguration (dict) --For CLOUDWATCH_METRIC health checks, a complex type that contains information about the CloudWatch alarm that you're associating with the health check.
            EvaluationPeriods (integer) --The number of periods over which data is compared to the specified threshold.
            Threshold (float) --The value that the metric is compared with to determine the state of the alarm. For example, if you want the health check to fail if the average TCP connection time is greater than 500 milliseconds for more than 60 seconds, the threshold is 500.
            ComparisonOperator (string) --The arithmetic operation to use when comparing the specified Statistic and Threshold.
            Valid Values are GreaterThanOrEqualToThreshold , GreaterThanThreshold , LessThanThreshold and LessThanOrEqualToThreshold
            Period (integer) --An integer that represents the period in seconds over which the statistic is applied.
            MetricName (string) --The name of the CloudWatch metric that is associated with the CloudWatch alarm.
            Namespace (string) --The namespace of the CloudWatch metric that is associated with the CloudWatch alarm.
            Statistic (string) --The statistic to apply to the CloudWatch metric that is associated with the CloudWatch alarm.
            Valid Values are SampleCount , Average , Sum , Minimum and Maximum
            Dimensions (list) --A list of Dimension elements for the CloudWatch metric that is associated with the CloudWatch alarm. For information about the metrics and dimensions that CloudWatch supports, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference .
            (dict) --The name and value of a dimension for a CloudWatch metric.
            Name (string) --The name of the dimension.
            Value (string) --The value of the dimension.
            
            
            
            
        :type HealthCheckId: string
        """
        self.client.get_health_check(HealthCheckId=HealthCheckId)

    def get_health_check_count(self):
        """
        """
        self.client.get_health_check_count()

    def get_health_check_last_failure_reason(self, HealthCheckId=None):
        """
        :param HealthCheckId: [REQUIRED]
            The ID of the health check for which you want to retrieve the reason for the most recent failure.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --A complex type that contains information about the most recent failure for the specified health check.
            HealthCheckObservations (list) --A list that contains one HealthCheckObservation element for each Amazon Route 53 health checker.
            (dict) --A complex type that contains the IP address of a Amazon Route 53 health checker and the reason for the health check status.
            Region (string) --The HealthCheckRegion of the Amazon Route 53 health checker that performed this health check.
            IPAddress (string) --The IP address of the Amazon Route 53 health checker that performed this health check.
            StatusReport (dict) --A complex type that contains information about the health check status for the current observation.
            Status (string) --The observed health check status.
            CheckedTime (datetime) --The date and time the health check status was observed, in the format YYYY-MM-DDThh:mm:ssZ , as specified in the ISO 8601 standard (for example, 2009-11-19T19:37:58Z). The Z after the time indicates that the time is listed in Coordinated Universal Time (UTC).
            
            
            
            
        :type HealthCheckId: string
        """
        self.client.get_health_check_last_failure_reason(HealthCheckId=HealthCheckId)

    def get_health_check_status(self, HealthCheckId=None):
        """
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
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --A complex type that contains information about the status of the specified health check.
            HealthCheckObservations (list) --A list that contains one HealthCheckObservation element for each Amazon Route 53 health checker.
            (dict) --A complex type that contains the IP address of a Amazon Route 53 health checker and the reason for the health check status.
            Region (string) --The HealthCheckRegion of the Amazon Route 53 health checker that performed this health check.
            IPAddress (string) --The IP address of the Amazon Route 53 health checker that performed this health check.
            StatusReport (dict) --A complex type that contains information about the health check status for the current observation.
            Status (string) --The observed health check status.
            CheckedTime (datetime) --The date and time the health check status was observed, in the format YYYY-MM-DDThh:mm:ssZ , as specified in the ISO 8601 standard (for example, 2009-11-19T19:37:58Z). The Z after the time indicates that the time is listed in Coordinated Universal Time (UTC).
            
            
            
            
        :type HealthCheckId: string
        """
        self.client.get_health_check_status(HealthCheckId=HealthCheckId)

    def get_hosted_zone(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the hosted zone for which you want to get a list of the name servers in the delegation set.
            Return typedict
            ReturnsResponse Syntax{
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
                  'VPCRegion': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
                  'VPCId': 'string'
                },
              ]
            }
            Response Structure
            (dict) --A complex type containing information about the specified hosted zone.
            HostedZone (dict) --A complex type that contains the information about the specified hosted zone.
            Id (string) --The ID of the specified hosted zone.
            Name (string) --The name of the domain. This must be a fully-specified domain, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            This is the name you have registered with your DNS registrar. You should ask your registrar to change the authoritative name servers for your domain to the set of NameServers elements returned in DelegationSet .
            CallerReference (string) --A unique string that identifies the request to create the hosted zone.
            Config (dict) --A complex type that contains the Comment element.
            Comment (string) --An optional comment about your hosted zone. If you don't want to specify a comment, you can omit the HostedZoneConfig and Comment elements from the XML document.
            PrivateZone (boolean) --GetHostedZone and ListHostedZone responses: A Boolean value that indicates whether a hosted zone is private.
            CreateHostedZone requests: When you're creating a private hosted zone (when you specify values for VPCId and VPCRegion), you can optionally specify true for PrivateZone.
            ResourceRecordSetCount (integer) --Total number of resource record sets in the hosted zone.
            DelegationSet (dict) --A complex type that contains information about the name servers for the specified hosted zone.
            Id (string) --
            CallerReference (string) --
            NameServers (list) --A complex type that contains the authoritative name servers for the hosted zone. Use the method provided by your domain registrar to add an NS record to your domain for each NameServer that is assigned to your hosted zone.
            (string) --
            
            VPCs (list) --A complex type that contains information about VPCs associated with the specified hosted zone.
            (dict) --
            VPCRegion (string) --
            VPCId (string) --A VPC ID
            
            
            
        :type Id: string
        """
        self.client.get_hosted_zone(Id=Id)

    def get_hosted_zone_count(self):
        """
        """
        self.client.get_hosted_zone_count()

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

    def get_reusable_delegation_set(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the reusable delegation set for which you want to get a list of the name server.
            Return typedict
            ReturnsResponse Syntax{
              'DelegationSet': {
                'Id': 'string',
                'CallerReference': 'string',
                'NameServers': [
                  'string',
                ]
              }
            }
            Response Structure
            (dict) --A complex type containing information about the specified reusable delegation set.
            DelegationSet (dict) --A complex type that contains the information about the nameservers for the specified delegation set ID.
            Id (string) --
            CallerReference (string) --
            NameServers (list) --A complex type that contains the authoritative name servers for the hosted zone. Use the method provided by your domain registrar to add an NS record to your domain for each NameServer that is assigned to your hosted zone.
            (string) --
            
            
            
        :type Id: string
        """
        self.client.get_reusable_delegation_set(Id=Id)

    def get_traffic_policy(self, Id=None, Version=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy that you want to get information about.
            
        :type Id: string
        :param Version: [REQUIRED]
            The version number of the traffic policy that you want to get information about.
            
        :type Version: integer
        """
        self.client.get_traffic_policy(Id=Id, Version=Version)

    def get_traffic_policy_instance(self, Id=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to get information about.
            Return typedict
            ReturnsResponse Syntax{
              'TrafficPolicyInstance': {
                'Id': 'string',
                'HostedZoneId': 'string',
                'Name': 'string',
                'TTL': 123,
                'State': 'string',
                'Message': 'string',
                'TrafficPolicyId': 'string',
                'TrafficPolicyVersion': 123,
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'PTR'|'SRV'|'SPF'|'AAAA'
              }
            }
            Response Structure
            (dict) --A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.
            TrafficPolicyInstance (dict) --A complex type that contains settings for the traffic policy instance.
            Id (string) --
            HostedZoneId (string) --
            Name (string) --
            TTL (integer) --
            State (string) --
            Message (string) --
            TrafficPolicyId (string) --
            TrafficPolicyVersion (integer) --
            TrafficPolicyType (string) --
            
            
        :type Id: string
        """
        self.client.get_traffic_policy_instance(Id=Id)

    def get_traffic_policy_instance_count(self):
        """
        """
        self.client.get_traffic_policy_instance_count()

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_change_batches_by_hosted_zone(self, HostedZoneId=None, StartDate=None, EndDate=None, MaxItems=None,
                                           Marker=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want to see changes for.
            
        :type HostedZoneId: string
        :param StartDate: [REQUIRED]
            The start of the time period you want to see changes for.
            
        :type StartDate: string
        :param EndDate: [REQUIRED]
            The end of the time period you want to see changes for.
            
        :type EndDate: string
        :param MaxItems: The maximum number of items on a page.
        :type MaxItems: string
        :param Marker: The page marker.
        :type Marker: string
        """
        self.client.list_change_batches_by_hosted_zone(HostedZoneId=HostedZoneId, StartDate=StartDate, EndDate=EndDate,
                                                       MaxItems=MaxItems, Marker=Marker)

    def list_change_batches_by_rr_set(self, HostedZoneId=None, Name=None, Type=None, SetIdentifier=None, StartDate=None,
                                      EndDate=None, MaxItems=None, Marker=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want to see changes for.
            
        :type HostedZoneId: string
        :param Name: [REQUIRED]
            The name of the RRSet that you want to see changes for.
            
        :type Name: string
        :param Type: [REQUIRED]
            The type of the RRSet that you want to see changes for.
            
        :type Type: string
        :param SetIdentifier: The identifier of the RRSet that you want to see changes for.
        :type SetIdentifier: string
        :param StartDate: [REQUIRED]
            The start of the time period you want to see changes for.
            
        :type StartDate: string
        :param EndDate: [REQUIRED]
            The end of the time period you want to see changes for.
            
        :type EndDate: string
        :param MaxItems: The maximum number of items on a page.
        :type MaxItems: string
        :param Marker: The page marker.
        :type Marker: string
        """
        self.client.list_change_batches_by_rr_set(HostedZoneId=HostedZoneId, Name=Name, Type=Type,
                                                  SetIdentifier=SetIdentifier, StartDate=StartDate, EndDate=EndDate,
                                                  MaxItems=MaxItems, Marker=Marker)

    def list_geo_locations(self, StartContinentCode=None, StartCountryCode=None, StartSubdivisionCode=None,
                           MaxItems=None):
        """
        :param StartContinentCode: The first continent code in the lexicographic ordering of geo locations that you want the ListGeoLocations request to list. For non-continent geo locations, this should be null.
            Valid values: AF | AN | AS | EU | OC | NA | SA
            Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
            
        :type StartContinentCode: string
        :param StartCountryCode: The first country code in the lexicographic ordering of geo locations that you want the ListGeoLocations request to list.
            The default geo location uses a * for the country code. All other country codes follow the ISO 3166 two-character code.
            
        :type StartCountryCode: string
        :param StartSubdivisionCode: The first subdivision code in the lexicographic ordering of geo locations that you want the ListGeoLocations request to list.
            Constraint: Specifying SubdivisionCode without CountryCode returns an InvalidInput error.
            
        :type StartSubdivisionCode: string
        :param MaxItems: The maximum number of geo locations you want in the response body.
        :type MaxItems: string
        """
        self.client.list_geo_locations(StartContinentCode=StartContinentCode, StartCountryCode=StartCountryCode,
                                       StartSubdivisionCode=StartSubdivisionCode, MaxItems=MaxItems)

    def list_health_checks(self, Marker=None, MaxItems=None):
        """
        :param Marker: If the request returned more than one page of results, submit another request and specify the value of NextMarker from the last response in the marker parameter to get the next page of results.
        :type Marker: string
        :param MaxItems: Specify the maximum number of health checks to return per page of results.
        :type MaxItems: string
        """
        self.client.list_health_checks(Marker=Marker, MaxItems=MaxItems)

    def list_hosted_zones(self, Marker=None, MaxItems=None, DelegationSetId=None):
        """
        :param Marker: If the request returned more than one page of results, submit another request and specify the value of NextMarker from the last response in the marker parameter to get the next page of results.
        :type Marker: string
        :param MaxItems: Specify the maximum number of hosted zones to return per page of results.
        :type MaxItems: string
        :param DelegationSetId: 
        :type DelegationSetId: string
        """
        self.client.list_hosted_zones(Marker=Marker, MaxItems=MaxItems, DelegationSetId=DelegationSetId)

    def list_hosted_zones_by_name(self, DNSName=None, HostedZoneId=None, MaxItems=None):
        """
        :param DNSName: The first name in the lexicographic ordering of domain names that you want the ListHostedZonesByNameRequest request to list.
            If the request returned more than one page of results, submit another request and specify the value of NextDNSName and NextHostedZoneId from the last response in the DNSName and HostedZoneId parameters to get the next page of results.
            
        :type DNSName: string
        :param HostedZoneId: If the request returned more than one page of results, submit another request and specify the value of NextDNSName and NextHostedZoneId from the last response in the DNSName and HostedZoneId parameters to get the next page of results.
        :type HostedZoneId: string
        :param MaxItems: Specify the maximum number of hosted zones to return per page of results.
        :type MaxItems: string
        """
        self.client.list_hosted_zones_by_name(DNSName=DNSName, HostedZoneId=HostedZoneId, MaxItems=MaxItems)

    def list_resource_record_sets(self, HostedZoneId=None, StartRecordName=None, StartRecordType=None,
                                  StartRecordIdentifier=None, MaxItems=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to get.
            
        :type HostedZoneId: string
        :param StartRecordName: The first name in the lexicographic ordering of domain names that you want the ListResourceRecordSets request to list.
        :type StartRecordName: string
        :param StartRecordType: The DNS type at which to begin the listing of resource record sets.
            Valid values: A | AAAA | CNAME | MX | NS | PTR | SOA | SPF | SRV | TXT
            Values for Weighted Resource Record Sets: A | AAAA | CNAME | TXT
            Values for Regional Resource Record Sets: A | AAAA | CNAME | TXT
            Values for Alias Resource Record Sets: A | AAAA
            Constraint: Specifying type without specifying name returns an InvalidInput error.
            
        :type StartRecordType: string
        :param StartRecordIdentifier: Weighted resource record sets only: If results were truncated for a given DNS name and type, specify the value of NextRecordIdentifier from the previous response to get the next resource record set that has the current DNS name and type.
        :type StartRecordIdentifier: string
        :param MaxItems: The maximum number of records you want in the response body.
        :type MaxItems: string
        """
        self.client.list_resource_record_sets(HostedZoneId=HostedZoneId, StartRecordName=StartRecordName,
                                              StartRecordType=StartRecordType,
                                              StartRecordIdentifier=StartRecordIdentifier, MaxItems=MaxItems)

    def list_reusable_delegation_sets(self, Marker=None, MaxItems=None):
        """
        :param Marker: If the request returned more than one page of results, submit another request and specify the value of NextMarker from the last response in the marker parameter to get the next page of results.
        :type Marker: string
        :param MaxItems: Specify the maximum number of reusable delegation sets to return per page of results.
        :type MaxItems: string
        """
        self.client.list_reusable_delegation_sets(Marker=Marker, MaxItems=MaxItems)

    def list_tags_for_resource(self, ResourceType=None, ResourceId=None):
        """
        :param ResourceType: [REQUIRED]
            The type of the resource.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            
        :type ResourceType: string
        :param ResourceId: [REQUIRED]
            The ID of the resource for which you want to retrieve tags.
            
        :type ResourceId: string
        """
        self.client.list_tags_for_resource(ResourceType=ResourceType, ResourceId=ResourceId)

    def list_tags_for_resources(self, ResourceType=None, ResourceIds=None):
        """
        :param ResourceType: [REQUIRED]
            The type of the resources.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            
        :type ResourceType: string
        :param ResourceIds: [REQUIRED]
            A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.
            (string) --
            
        :type ResourceIds: list
        """
        self.client.list_tags_for_resources(ResourceType=ResourceType, ResourceIds=ResourceIds)

    def list_traffic_policies(self, TrafficPolicyIdMarker=None, MaxItems=None):
        """
        :param TrafficPolicyIdMarker: For your first request to ListTrafficPolicies , do not include the TrafficPolicyIdMarker parameter.
            If you have more traffic policies than the value of MaxItems , ListTrafficPolicies returns only the first MaxItems traffic policies. To get the next group of MaxItems policies, submit another request to ListTrafficPolicies . For the value of TrafficPolicyIdMarker , specify the value of the TrafficPolicyIdMarker element that was returned in the previous response.
            Policies are listed in the order in which they were created.
            
        :type TrafficPolicyIdMarker: string
        :param MaxItems: The maximum number of traffic policies to be included in the response body for this request. If you have more than MaxItems traffic policies, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyIdMarker element is the ID of the first traffic policy in the next group of MaxItems traffic policies.
        :type MaxItems: string
        """
        self.client.list_traffic_policies(TrafficPolicyIdMarker=TrafficPolicyIdMarker, MaxItems=MaxItems)

    def list_traffic_policy_instances(self, HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None,
                                      TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
        """
        :param HostedZoneIdMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get the next group of MaxItems traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of HostedZoneIdMarker , specify the value of HostedZoneIdMarker from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            
        :type HostedZoneIdMarker: string
        :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            
        :type TrafficPolicyInstanceNameMarker: string
        :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstances , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.
            
        :type TrafficPolicyInstanceTypeMarker: string
        :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
        :type MaxItems: string
        """
        self.client.list_traffic_policy_instances(HostedZoneIdMarker=HostedZoneIdMarker,
                                                  TrafficPolicyInstanceNameMarker=TrafficPolicyInstanceNameMarker,
                                                  TrafficPolicyInstanceTypeMarker=TrafficPolicyInstanceTypeMarker,
                                                  MaxItems=MaxItems)

    def list_traffic_policy_instances_by_hosted_zone(self, HostedZoneId=None, TrafficPolicyInstanceNameMarker=None,
                                                     TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
        """
        :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone for which you want to list traffic policy instances.
            
        :type HostedZoneId: string
        :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            
        :type TrafficPolicyInstanceNameMarker: string
        :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstancesByHostedZone , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            
        :type TrafficPolicyInstanceTypeMarker: string
        :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
        :type MaxItems: string
        """
        self.client.list_traffic_policy_instances_by_hosted_zone(HostedZoneId=HostedZoneId,
                                                                 TrafficPolicyInstanceNameMarker=TrafficPolicyInstanceNameMarker,
                                                                 TrafficPolicyInstanceTypeMarker=TrafficPolicyInstanceTypeMarker,
                                                                 MaxItems=MaxItems)

    def list_traffic_policy_instances_by_policy(self, TrafficPolicyId=None, TrafficPolicyVersion=None,
                                                HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None,
                                                TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
        """
        :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy for which you want to list traffic policy instances.
            
        :type TrafficPolicyId: string
        :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by TrafficPolicyId .
            
        :type TrafficPolicyVersion: integer
        :param HostedZoneIdMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , HostedZoneIdMarker is the ID of the hosted zone for the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            
        :type HostedZoneIdMarker: string
        :param TrafficPolicyInstanceNameMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            If the value of IsTruncated in the previous response was false , omit this value.
            
        :type TrafficPolicyInstanceNameMarker: string
        :param TrafficPolicyInstanceTypeMarker: For the first request to ListTrafficPolicyInstancesByPolicy , omit this value.
            If the value of IsTruncated in the previous response was true , TrafficPolicyInstanceTypeMarker is the DNS type of the first traffic policy instance in the next group of MaxItems traffic policy instances.
            If the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get for this hosted zone.
            
        :type TrafficPolicyInstanceTypeMarker: string
        :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.
        :type MaxItems: string
        """
        self.client.list_traffic_policy_instances_by_policy(TrafficPolicyId=TrafficPolicyId,
                                                            TrafficPolicyVersion=TrafficPolicyVersion,
                                                            HostedZoneIdMarker=HostedZoneIdMarker,
                                                            TrafficPolicyInstanceNameMarker=TrafficPolicyInstanceNameMarker,
                                                            TrafficPolicyInstanceTypeMarker=TrafficPolicyInstanceTypeMarker,
                                                            MaxItems=MaxItems)

    def list_traffic_policy_versions(self, Id=None, TrafficPolicyVersionMarker=None, MaxItems=None):
        """
        :param Id: [REQUIRED]
            Specify the value of Id of the traffic policy for which you want to list all versions.
            
        :type Id: string
        :param TrafficPolicyVersionMarker: For your first request to ListTrafficPolicyVersions , do not include the TrafficPolicyVersionMarker parameter.
            If you have more traffic policy versions than the value of MaxItems , ListTrafficPolicyVersions returns only the first group of MaxItems versions. To get the next group of MaxItems traffic policy versions, submit another request to ListTrafficPolicyVersions . For the value of TrafficPolicyVersionMarker , specify the value of the TrafficPolicyVersionMarker element that was returned in the previous response.
            Traffic policy versions are listed in sequential order.
            
        :type TrafficPolicyVersionMarker: string
        :param MaxItems: The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than MaxItems versions, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyVersionMarker element is the ID of the first version in the next group of MaxItems traffic policy versions.
        :type MaxItems: string
        """
        self.client.list_traffic_policy_versions(Id=Id, TrafficPolicyVersionMarker=TrafficPolicyVersionMarker,
                                                 MaxItems=MaxItems)

    def update_health_check(self, HealthCheckId=None, HealthCheckVersion=None, IPAddress=None, Port=None,
                            ResourcePath=None, FullyQualifiedDomainName=None, SearchString=None, FailureThreshold=None,
                            Inverted=None, HealthThreshold=None, ChildHealthChecks=None, EnableSNI=None, Regions=None,
                            AlarmIdentifier=None, InsufficientDataHealthStatus=None):
        """
        :param HealthCheckId: [REQUIRED]
            The ID of the health check to update.
            
        :type HealthCheckId: string
        :param HealthCheckVersion: Optional. When you specify a health check version, Amazon Route 53 compares this value with the current value in the health check, which prevents you from updating the health check when the versions don't match. Using HealthCheckVersion lets you prevent overwriting another change to the health check.
        :type HealthCheckVersion: integer
        :param IPAddress: The IP address of the resource that you want to check.
            Specify this value only if you want to change it.
            
        :type IPAddress: string
        :param Port: The port on which you want Amazon Route 53 to open a connection to perform health checks.
            Specify this value only if you want to change it.
            
        :type Port: integer
        :param ResourcePath: The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.
            Specify this value only if you want to change it.
            
        :type ResourcePath: string
        :param FullyQualifiedDomainName: Fully qualified domain name of the instance to be health checked.
            Specify this value only if you want to change it.
            
        :type FullyQualifiedDomainName: string
        :param SearchString: If the value of Type is HTTP_STR_MATCH or HTTP_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy. Amazon Route 53 considers case when searching for SearchString in the response body.
            Specify this value only if you want to change it.
            
        :type SearchString: string
        :param FailureThreshold: The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.
            Valid values are integers between 1 and 10. For more information, see 'How Amazon Route 53 Determines Whether an Endpoint Is Healthy' in the Amazon Route 53 Developer Guide.
            Specify this value only if you want to change it.
            
        :type FailureThreshold: integer
        :param Inverted: A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Amazon Route 53 considers the health check to be unhealthy.
            Specify this value only if you want to change it.
            
        :type Inverted: boolean
        :param HealthThreshold: The minimum number of child health checks that must be healthy for Amazon Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive.
            Specify this value only if you want to change it.
            
        :type HealthThreshold: integer
        :param ChildHealthChecks: For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
            Specify this value only if you want to change it.
            (string) --
            
        :type ChildHealthChecks: list
        :param EnableSNI: Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. If you don't specify a value for EnableSNI , Amazon Route 53 defaults to true when Type is HTTPS or HTTPS_STR_MATCH and defaults to false when Type is any other value.
            Specify this value only if you want to change it.
            
        :type EnableSNI: boolean
        :param Regions: A list of HealthCheckRegion values that specify the Amazon EC2 regions that you want Amazon Route 53 to use to perform health checks. You must specify at least three regions.
            Note
            When you remove a region from the list, Amazon Route 53 will briefly continue to check your endpoint from that region.
            Specify this value only if you want to change it.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            
        :type Regions: list
        :param AlarmIdentifier: A complex type that contains information to uniquely identify the CloudWatch alarm that you're associating with a Route 53 health check.
            Region (string) -- [REQUIRED]The CloudWatchRegion that the CloudWatch alarm was created in.
            Name (string) -- [REQUIRED]The name of the CloudWatch alarm.
            
        :type AlarmIdentifier: dict
        :param InsufficientDataHealthStatus: 
        :type InsufficientDataHealthStatus: string
        """
        self.client.update_health_check(HealthCheckId=HealthCheckId, HealthCheckVersion=HealthCheckVersion,
                                        IPAddress=IPAddress, Port=Port, ResourcePath=ResourcePath,
                                        FullyQualifiedDomainName=FullyQualifiedDomainName, SearchString=SearchString,
                                        FailureThreshold=FailureThreshold, Inverted=Inverted,
                                        HealthThreshold=HealthThreshold, ChildHealthChecks=ChildHealthChecks,
                                        EnableSNI=EnableSNI, Regions=Regions, AlarmIdentifier=AlarmIdentifier,
                                        InsufficientDataHealthStatus=InsufficientDataHealthStatus)

    def update_hosted_zone_comment(self, Id=None, Comment=None):
        """
        :param Id: [REQUIRED]
            The ID of the hosted zone you want to update.
            
        :type Id: string
        :param Comment: A comment about your hosted zone.
        :type Comment: string
        """
        self.client.update_hosted_zone_comment(Id=Id, Comment=Comment)

    def update_traffic_policy_comment(self, Id=None, Version=None, Comment=None):
        """
        :param Id: [REQUIRED]
            The value of Id for the traffic policy for which you want to update the comment.
            
        :type Id: string
        :param Version: [REQUIRED]
            The value of Version for the traffic policy for which you want to update the comment.
            
        :type Version: integer
        :param Comment: [REQUIRED]
            The new comment for the specified traffic policy and version.
            
        :type Comment: string
        """
        self.client.update_traffic_policy_comment(Id=Id, Version=Version, Comment=Comment)

    def update_traffic_policy_instance(self, Id=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
        """
        :param Id: [REQUIRED]
            The ID of the traffic policy instance that you want to update.
            
        :type Id: string
        :param TTL: [REQUIRED]
            The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.
            
        :type TTL: integer
        :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
            
        :type TrafficPolicyId: string
        :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
            
        :type TrafficPolicyVersion: integer
        """
        self.client.update_traffic_policy_instance(Id=Id, TTL=TTL, TrafficPolicyId=TrafficPolicyId,
                                                   TrafficPolicyVersion=TrafficPolicyVersion)
