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


def associate_vpc_with_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone you want to associate your VPC with.
            Note that you cannot associate a VPC with a hosted zone that doesn't have an existing VPC association.
            
    :type HostedZoneId: string
    :param VPC: [REQUIRED]
            A complex type containing information about the Amazon VPC that you're associating with the specified hosted zone.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            
    :type VPC: dict
    :param Comment: Optional: A comment about the association request.
    :type Comment: string
    """
    pass


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


def change_resource_record_sets(HostedZoneId=None, ChangeBatch=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to change.
            
    :type HostedZoneId: string
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
            
            
            
    :type ChangeBatch: dict
    """
    pass


def change_tags_for_resource(ResourceType=None, ResourceId=None, AddTags=None, RemoveTagKeys=None):
    """
    :param ResourceType: [REQUIRED]
            The type of the resource.
            The resource type for health checks is healthcheck .
            The resource type for hosted zones is hostedzone .
            
    :type ResourceType: string
    :param ResourceId: [REQUIRED]
            The ID of the resource for which you want to add, change, or delete tags.
            
    :type ResourceId: string
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
            
            
    :type AddTags: list
    :param RemoveTagKeys: A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.
            (string) --
            
    :type RemoveTagKeys: list
    """
    pass


def create_health_check(CallerReference=None, HealthCheckConfig=None):
    """
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHealthCheck requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a health check.
            
    :type CallerReference: string
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
            
    :type HealthCheckConfig: dict
    """
    pass


def create_hosted_zone(Name=None, VPC=None, CallerReference=None, HostedZoneConfig=None, DelegationSetId=None):
    """
    :param Name: [REQUIRED]
            The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Amazon Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in the DelegationSet element.
            
    :type Name: string
    :param VPC: The VPC that you want your hosted zone to be associated with. By providing this parameter, your newly created hosted cannot be resolved anywhere other than the given VPC.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            
    :type VPC: dict
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you create a hosted zone. CallerReference can be any unique string, for example, a date/time stamp.
            
    :type CallerReference: string
    :param HostedZoneConfig: (Optional) A complex type that contains an optional comment about your hosted zone. If you don't want to specify a comment, omit both the HostedZoneConfig and Comment elements.
            Comment (string) --Any comments that you want to include about the hosted zone.
            PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.
            
    :type HostedZoneConfig: dict
    :param DelegationSetId: If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see CreateReusableDelegationSet .
            Type
            String
            Default
            None
            Parent
            CreatedHostedZoneRequest
            
    :type DelegationSetId: string
    """
    pass


def create_reusable_delegation_set(CallerReference=None, HostedZoneId=None):
    """
    :param CallerReference: [REQUIRED]
            A unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example a date/time stamp.
            
    :type CallerReference: string
    :param HostedZoneId: If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.
    :type HostedZoneId: string
    """
    pass


def create_traffic_policy(Name=None, Document=None, Comment=None):
    """
    :param Name: [REQUIRED]
            The name of the traffic policy.
            
    :type Name: string
    :param Document: [REQUIRED]
            The definition of this traffic policy in JSON format. For more information, see Traffic Policy Document Format in the Amazon Route 53 API Reference .
            
    :type Document: string
    :param Comment: (Optional) Any comments that you want to include about the traffic policy.
    :type Comment: string
    """
    pass


def create_traffic_policy_instance(HostedZoneId=None, Name=None, TTL=None, TrafficPolicyId=None,
                                   TrafficPolicyVersion=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone in which you want Amazon Route 53 to create resource record sets by using the configuration in a traffic policy.
            
    :type HostedZoneId: string
    :param Name: [REQUIRED]
            The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Amazon Route 53 creates for this traffic policy instance.
            
    :type Name: string
    :param TTL: [REQUIRED]
            (Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.
            
    :type TTL: integer
    :param TrafficPolicyId: [REQUIRED]
            The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            
    :type TrafficPolicyId: string
    :param TrafficPolicyVersion: [REQUIRED]
            The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
            
    :type TrafficPolicyVersion: integer
    """
    pass


def create_traffic_policy_version(Id=None, Document=None, Comment=None):
    """
    :param Id: [REQUIRED]
            The ID of the traffic policy for which you want to create a new version.
            
    :type Id: string
    :param Document: [REQUIRED]
            The definition of this version of the traffic policy, in JSON format. You specified the JSON in the CreateTrafficPolicyVersion request. For more information about the JSON format, see CreateTrafficPolicy .
            
    :type Document: string
    :param Comment: The comment that you specified in the CreateTrafficPolicyVersion request, if any.
    :type Comment: string
    """
    pass


def delete_health_check(HealthCheckId=None):
    """
    :param HealthCheckId: [REQUIRED]
            The ID of the health check that you want to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element.
            
            
    :type HealthCheckId: string
    """
    pass


def delete_hosted_zone(Id=None):
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
            Id (string) --The ID of the request.
            Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
            SubmittedAt (datetime) --The date and time the change request was submitted, in Coordinated Universal Time (UTC) format: YYYY-MM-DDThh:mm:ssZ . For more information, see the Wikipedia entry ISO 8601 .
            Comment (string) --A complex type that describes change information about changes made to your hosted zone.
            This element contains an ID that you use when performing a GetChange action to get detailed information about the change.
            
            
            
    :type Id: string
    """
    pass


def delete_reusable_delegation_set(Id=None):
    """
    :param Id: [REQUIRED]
            The ID of the reusable delegation set you want to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element.
            
            
    :type Id: string
    """
    pass


def delete_traffic_policy(Id=None, Version=None):
    """
    :param Id: [REQUIRED]
            The ID of the traffic policy that you want to delete.
            
    :type Id: string
    :param Version: [REQUIRED]
            The version number of the traffic policy that you want to delete.
            
    :type Version: integer
    """
    pass


def delete_traffic_policy_instance(Id=None):
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
    pass


def disassociate_vpc_from_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the VPC that you want to disassociate from an Amazon Route 53 hosted zone.
            
    :type HostedZoneId: string
    :param VPC: [REQUIRED]
            A complex type containing information about the Amazon VPC that you're disassociating from the specified hosted zone.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            
    :type VPC: dict
    :param Comment: Optional: A comment about the disassociation request.
    :type Comment: string
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


def get_change(Id=None):
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
            ChangeInfo (dict) --A complex type that contains information about the specified change batch.
            Id (string) --The ID of the request.
            Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
            SubmittedAt (datetime) --The date and time the change request was submitted, in Coordinated Universal Time (UTC) format: YYYY-MM-DDThh:mm:ssZ . For more information, see the Wikipedia entry ISO 8601 .
            Comment (string) --A complex type that describes change information about changes made to your hosted zone.
            This element contains an ID that you use when performing a GetChange action to get detailed information about the change.
            
            
            
    :type Id: string
    """
    pass


def get_change_details(Id=None):
    """
    :param Id: [REQUIRED]
            The ID of the change batch. This is the value that you specified in the change ID parameter when you submitted the request.
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
            (dict) --The information for each resource record set that you want to change.
            Action (string) --The action to perform:
            CREATE : Creates a resource record set that has the specified values.
            DELETE : Deletes a existing resource record set that has the specified values for Name , Type , SetIdentifier (for latency, weighted, geolocation, and failover resource record sets), and TTL (except alias resource record sets, for which the TTL is determined by the AWS resource that you're routing DNS queries to).
            Warning
            To delete the resource record set that is associated with a traffic policy instance, use `` DeleteTrafficPolicyInstance `` . Amazon Route 53will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Amazon Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use.
            UPSERT : If a resource record set does not already exist, Amazon Route 53 creates it. If a resource record set does exist, Amazon Route 53 updates it with the values in the request. Amazon Route 53 can update an existing resource record set only when all of the following values match: Name , Type , and SetIdentifier (for weighted, latency, geolocation, and failover resource record sets).
            ResourceRecordSet (dict) --Information about the resource record set to create or delete.
            Name (string) --The name of the domain you want to perform the action on.
            Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 still assumes that the domain name that you specify is fully qualified. This means that Amazon Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
            For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
            You can use the asterisk (*) wildcard to replace the leftmost label in a domain name. For example, *.example.com . Note the following:
            The * must replace the entire label. For example, you can't specify *prod.example.com or prod*.example.com .
            The * can't replace any of the middle labels, for example, marketing.*.example.com.
            If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
            Warning
            You can't use the * wildcard for resource records sets that have a type of NS.
            You can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You cannot use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can't specify prod*.example.com .
            Type (string) --The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
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
            Value (string) --The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
            You can specify more than one value for all record types except CNAME and SOA .
            Note
            If you are creating an alias resource record set, omit Value .
            
            AliasTarget (dict) --
            Alias resource record sets only: Information about the CloudFront distribution, Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you are redirecting queries. The Elastic Beanstalk environment must have a regionalized subdomain.
            If you're creating resource records sets for a private hosted zone, note the following:
            You can't create alias resource record sets for CloudFront distributions in a private hosted zone.
            Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.
            For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .
            HostedZoneId (string) --
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
            DNSName (string) --
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
            EvaluateTargetHealth (boolean) --
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
            
            
            
            
    :type Id: string
    """
    pass


def get_checker_ip_ranges():
    """
    """
    pass


def get_geo_location(ContinentCode=None, CountryCode=None, SubdivisionCode=None):
    """
    :param ContinentCode: Amazon Route 53 supports the following continent codes:
            AF : Africa
            AN : Antarctica
            AS : Asia
            EU : Europe
            OC : Oceania
            NA : North America
            SA : South America
            
    :type ContinentCode: string
    :param CountryCode: Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .
    :type CountryCode: string
    :param SubdivisionCode: Amazon Route 53 uses the one- to three-letter subdivision codes that are specified in ISO standard 3166-1 alpha-2 . Amazon Route 53 doesn't support subdivision codes for all countries. If you specify SubdivisionCode , you must also specify CountryCode .
    :type SubdivisionCode: string
    """
    pass


def get_health_check(HealthCheckId=None):
    """
    :param HealthCheckId: [REQUIRED]
            The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
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
            Response Structure
            (dict) --A complex type that contains the response to a GetHealthCheck request.
            HealthCheck (dict) --A complex type that contains information about one health check that is associated with the current AWS account.
            Id (string) --The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
            CallerReference (string) --A unique string that you specified when you created the health check.
            HealthCheckConfig (dict) --A complex type that contains detailed information about one health check.
            IPAddress (string) --The IPv4 IP address of the endpoint on which you want Amazon Route 53 to perform health checks. If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval. Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            If the endpoint is an Amazon EC2 instance, we recommend that you create an Elastic IP address, associate it with your Amazon EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
            For more information, see HealthCheckConfig$FullyQualifiedDomainName .
            Contraints: Amazon Route 53 cannot check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you cannot create health checks, see RFC 5735, Special Use IPv4 Addresses and RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space .
            When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress.
            Port (integer) --The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for Port only when you specify a value for IPAddress .
            Type (string) --The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.
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
            Region (string) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            For the current list of CloudWatch regions, see Amazon CloudWatch in AWS Regions and Endpoints in the Amazon Web Services General Reference .
            Name (string) --The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            InsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
            Healthy : Amazon Route 53 considers the health check to be healthy.
            Unhealthy : Amazon Route 53 considers the health check to be unhealthy.
            LastKnownStatus : Amazon Route 53uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
            
            HealthCheckVersion (integer) --The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.
            CloudWatchAlarmConfiguration (dict) --A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.
            EvaluationPeriods (integer) --For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.
            Threshold (float) --For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.
            ComparisonOperator (string) --For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.
            Period (integer) --For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.
            MetricName (string) --The name of the CloudWatch metric that the alarm is associated with.
            Namespace (string) --The namespace of the metric that the alarm is associated with. For more information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch Developer Guide .
            Statistic (string) --For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.
            Dimensions (list) --For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric.For information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch Developer Guide .
            (dict) --For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.
            Name (string) --For the metric that the CloudWatch alarm is associated with, the name of one dimension.
            Value (string) --For the metric that the CloudWatch alarm is associated with, the value of one dimension.
            
            
            
            
    :type HealthCheckId: string
    """
    pass


def get_health_check_count():
    """
    """
    pass


def get_health_check_last_failure_reason(HealthCheckId=None):
    """
    :param HealthCheckId: [REQUIRED]
            The ID for the health check for which you want the last failure reason. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.
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
            (dict) --A complex type that contains the response to a GetHealthCheckLastFailureReason request.
            HealthCheckObservations (list) --A list that contains one Observation element for each Amazon Route 53 health checker that is reporting a last failure reason.
            (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.
            Region (string) --The region of the Amazon Route 53 health checker that provided the status in StatusReport.
            IPAddress (string) --The IP address of the Amazon Route 53 health checker that provided the failure reason in StatusReport .
            StatusReport (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.
            Status (string) --A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.
            CheckedTime (datetime) --The time at which the health checker performed the health check in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2014-10-27T17:48:16.751Z represents October 27, 2014 at 17:48:16.751 UTC.
            
            
            
            
    :type HealthCheckId: string
    """
    pass


def get_health_check_status(HealthCheckId=None):
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
            (dict) --A complex type that contains the response to a GetHealthCheck request.
            HealthCheckObservations (list) --A list that contains one HealthCheckObservation element for each Amazon Route 53 health checker that is reporting a status about the health check endpoint.
            (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.
            Region (string) --The region of the Amazon Route 53 health checker that provided the status in StatusReport.
            IPAddress (string) --The IP address of the Amazon Route 53 health checker that provided the failure reason in StatusReport .
            StatusReport (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.
            Status (string) --A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.
            CheckedTime (datetime) --The time at which the health checker performed the health check in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2014-10-27T17:48:16.751Z represents October 27, 2014 at 17:48:16.751 UTC.
            
            
            
            
    :type HealthCheckId: string
    """
    pass


def get_hosted_zone(Id=None):
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
                  'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'sa-east-1'|'cn-north-1',
                  'VPCId': 'string'
                },
              ]
            }
            Response Structure
            (dict) --A complex type containing the response information for the hosted zone.
            HostedZone (dict) --A complex type that contains general information about the hosted zone.
            Id (string) --The ID that Amazon Route 53 assigned to the hosted zone when you created it.
            Name (string) --The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
            For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .
            CallerReference (string) --The value that you specified for CallerReference when you created the hosted zone.
            Config (dict) --A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don't appear in the response.
            Comment (string) --Any comments that you want to include about the hosted zone.
            PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.
            ResourceRecordSetCount (integer) --The number of resource record sets in the hosted zone.
            DelegationSet (dict) --A complex type that describes the name servers for this hosted zone.
            Id (string) --The ID that Amazon Route 53 assigns to a reusable delegation set.
            CallerReference (string) --A unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example, a date/time stamp.
            NameServers (list) --A complex type that contains a list of the authoritative name servers for the hosted zone.
            (string) --
            
            VPCs (list) --A complex type that contains information about VPCs associated with the specified hosted zone.
            (dict) --A complex type that contains information about the Amazon VPC that you're associating with the specified hosted zone.
            VPCRegion (string) --The region in which you created the VPC that you want to associate with the specified Amazon Route 53 hosted zone.
            VPCId (string) --A VPC ID
            
            
            
    :type Id: string
    """
    pass


def get_hosted_zone_count():
    """
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


def get_reusable_delegation_set(Id=None):
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
            (dict) --A complex type that contains the response to the GetReusableDelegationSet request.
            DelegationSet (dict) --A complex type that contains information about the reusable delegation set.
            Id (string) --The ID that Amazon Route 53 assigns to a reusable delegation set.
            CallerReference (string) --A unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example, a date/time stamp.
            NameServers (list) --A complex type that contains a list of the authoritative name servers for the hosted zone.
            (string) --
            
            
            
    :type Id: string
    """
    pass


def get_traffic_policy(Id=None, Version=None):
    """
    :param Id: [REQUIRED]
            The ID of the traffic policy that you want to get information about.
            
    :type Id: string
    :param Version: [REQUIRED]
            The version number of the traffic policy that you want to get information about.
            
    :type Version: integer
    """
    pass


def get_traffic_policy_instance(Id=None):
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
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'
              }
            }
            Response Structure
            (dict) --A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.
            TrafficPolicyInstance (dict) --A complex type that contains settings for the traffic policy instance.
            Id (string) --The ID that Amazon Route 53 assigned to the new traffic policy instance.
            HostedZoneId (string) --The ID of the hosted zone that Amazon Route 53 created resource record sets in.
            Name (string) --The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.
            TTL (integer) --The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.
            State (string) --The value of State is one of the following values:
            Applied
            Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Amazon Route 53 edge locations.
            Creating
            Amazon Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.
            Failed
            Amazon Route 53 wasn't able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.
            Message (string) --If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.
            TrafficPolicyId (string) --The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
            TrafficPolicyVersion (integer) --The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
            TrafficPolicyType (string) --The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.
            
            
            
    :type Id: string
    """
    pass


def get_traffic_policy_instance_count():
    """
    """
    pass


def get_waiter():
    """
    """
    pass


def list_change_batches_by_hosted_zone(HostedZoneId=None, StartDate=None, EndDate=None, MaxItems=None, Marker=None):
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
    pass


def list_change_batches_by_rr_set(HostedZoneId=None, Name=None, Type=None, SetIdentifier=None, StartDate=None,
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
    pass


def list_geo_locations(StartContinentCode=None, StartCountryCode=None, StartSubdivisionCode=None, MaxItems=None):
    """
    :param StartContinentCode: The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true, and if NextContinentCode from the previous response has a value, enter that value in StartContinentCode to return the next page of results.
            Include StartContinentCode only if you want to list continents. Don't include StartContinentCode when you're listing countries or countries with their subdivisions.
            
    :type StartContinentCode: string
    :param StartCountryCode: The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextCountryCode from the previous response has a value, enter that value in StartCountryCode to return the next page of results.
            Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .
            
    :type StartCountryCode: string
    :param StartSubdivisionCode: The code for the subdivision (for example, state or province) with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Amazon Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextSubdivisionCode from the previous response has a value, enter that value in StartSubdivisionCode to return the next page of results.
            To list subdivisions of a country, you must include both StartCountryCode and StartSubdivisionCode .
            
    :type StartSubdivisionCode: string
    :param MaxItems: (Optional) The maximum number of geolocations to be included in the response body for this request. If more than MaxItems geolocations remain to be listed, then the value of the IsTruncated element in the response is true .
    :type MaxItems: string
    """
    pass


def list_health_checks(Marker=None, MaxItems=None):
    """
    :param Marker: If the response to a ListHealthChecks is more than one page, marker is the health check ID for the first health check on the next page of results. For more information, see ListHealthChecksResponse$MaxItems .
    :type Marker: string
    :param MaxItems: The maximum number of HealthCheck elements you want ListHealthChecks to return on each page of the response body. If the AWS account includes more HealthCheck elements than the value of maxitems , the response is broken into pages. Each page contains the number of HealthCheck elements specified by maxitems .
            For example, suppose you specify 10 for maxitems and the current AWS account has 51 health checks. In the response, ListHealthChecks sets ListHealthChecksResponse$IsTruncated to true and includes the ListHealthChecksResponse$NextMarker element. To access the second and subsequent pages, you resend the GET ListHealthChecks request, add the ListHealthChecksResponse$Marker parameter to the request, and specify the value of the ListHealthChecksResponse$NextMarker element from the previous response. On the last (sixth) page of the response, which contains only one HealthCheck element:
            The value of ListHealthChecksResponse$IsTruncated is false .
            ListHealthChecksResponse$NextMarker is omitted.
            
    :type MaxItems: string
    """
    pass


def list_hosted_zones(Marker=None, MaxItems=None, DelegationSetId=None):
    """
    :param Marker: (Optional) If you have more hosted zones than the value of maxitems , ListHostedZones returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZones . For the value of marker, specify the value of the NextMarker element that was returned in the previous response.
            Hosted zones are listed in the order in which they were created.
            
    :type Marker: string
    :param MaxItems: (Optional) The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, the value of the IsTruncated element in the response is true , and the value of the NextMarker element is the hosted zone ID of the first hosted zone in the next group of maxitems hosted zones.
    :type MaxItems: string
    :param DelegationSetId: If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.
    :type DelegationSetId: string
    """
    pass


def list_hosted_zones_by_name(DNSName=None, HostedZoneId=None, MaxItems=None):
    """
    :param DNSName: (Optional) For your first request to ListHostedZonesByName , include the dnsname parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the dnsname parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both dnsname and hostedzoneid parameters. For dnsname , specify the value of NextDNSName from the previous response.
    :type DNSName: string
    :param HostedZoneId: (Optional) For your first request to ListHostedZonesByName , do not include the hostedzoneid parameter.
            If you have more hosted zones than the value of maxitems , ListHostedZonesByName returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZonesByName and include both dnsname and hostedzoneid parameters. For the value of hostedzoneid , specify the value of the NextHostedZoneId element from the previous response.
            
    :type HostedZoneId: string
    :param MaxItems: The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, then the value of the IsTruncated element in the response is true, and the values of NextDNSName and NextHostedZoneId specify the first hosted zone in the next group of maxitems hosted zones.
    :type MaxItems: string
    """
    pass


def list_resource_record_sets(HostedZoneId=None, StartRecordName=None, StartRecordType=None, StartRecordIdentifier=None,
                              MaxItems=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that contains the resource record sets that you want to get.
            
    :type HostedZoneId: string
    :param StartRecordName: The first name in the lexicographic ordering of domain names that you want the ListResourceRecordSets request to list.
    :type StartRecordName: string
    :param StartRecordType: The type of resource record set to begin the record listing from.
            Valid values for basic resource record sets: A | AAAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
            Values for weighted, latency, geo, and failover resource record sets: A | AAAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT
            Values for alias resource record sets:
            CloudFront distribution : A
            Elastic Beanstalk environment that has a regionalized subdomain : A
            ELB load balancer : A | AAAA
            Amazon S3 bucket : A
            Constraint: Specifying type without specifying name returns an InvalidInput error.
            
    :type StartRecordType: string
    :param StartRecordIdentifier: Weighted resource record sets only: If results were truncated for a given DNS name and type, specify the value of NextRecordIdentifier from the previous response to get the next resource record set that has the current DNS name and type.
    :type StartRecordIdentifier: string
    :param MaxItems: (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than maxitems resource record sets, the value of the IsTruncated element in the response is true , and the values of the NextRecordName and NextRecordType elements in the response identify the first resource record set in the next group of maxitems resource record sets.
    :type MaxItems: string
    """
    pass


def list_reusable_delegation_sets(Marker=None, MaxItems=None):
    """
    :param Marker: If you're making the second or subsequent call to ListReusableDelegationSets , the Marker element matches the value that you specified in the marker parameter in the previous request.
    :type Marker: string
    :param MaxItems: The value that you specified for the maxitems parameter in the request that produced the current response.
    :type MaxItems: string
    """
    pass


def list_tags_for_resource(ResourceType=None, ResourceId=None):
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
    pass


def list_tags_for_resources(ResourceType=None, ResourceIds=None):
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
    pass


def list_traffic_policies(TrafficPolicyIdMarker=None, MaxItems=None):
    """
    :param TrafficPolicyIdMarker: (Conditional) For your first request to ListTrafficPolicies , do not include the TrafficPolicyIdMarker parameter.
            If you have more traffic policies than the value of MaxItems , ListTrafficPolicies returns only the first MaxItems traffic policies. To get the next group of MaxItems policies, submit another request to ListTrafficPolicies . For the value of TrafficPolicyIdMarker , specify the value of the TrafficPolicyIdMarker element that was returned in the previous response.
            Policies are listed in the order in which they were created.
            
    :type TrafficPolicyIdMarker: string
    :param MaxItems: (Optional) The maximum number of traffic policies to be included in the response body for this request. If you have more than MaxItems traffic policies, the value of the IsTruncated element in the response is true , and the value of the TrafficPolicyIdMarker element is the ID of the first traffic policy in the next group of MaxItems traffic policies.
    :type MaxItems: string
    """
    pass


def list_traffic_policy_instances(HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None,
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
    pass


def list_traffic_policy_instances_by_hosted_zone(HostedZoneId=None, TrafficPolicyInstanceNameMarker=None,
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
    pass


def list_traffic_policy_instances_by_policy(TrafficPolicyId=None, TrafficPolicyVersion=None, HostedZoneIdMarker=None,
                                            TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None,
                                            MaxItems=None):
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
    pass


def list_traffic_policy_versions(Id=None, TrafficPolicyVersionMarker=None, MaxItems=None):
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
    pass


def test_dns_answer(HostedZoneId=None, RecordName=None, RecordType=None, ResolverIP=None, EDNS0ClientSubnetIP=None,
                    EDNS0ClientSubnetMask=None):
    """
    :param HostedZoneId: [REQUIRED]
            The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
            
    :type HostedZoneId: string
    :param RecordName: [REQUIRED]
            The name of the resource record set that you want Amazon Route 53 to simulate a query for.
            
    :type RecordName: string
    :param RecordType: [REQUIRED]
            The type of the resource record set.
            
    :type RecordType: string
    :param ResolverIP: If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, TestDnsAnswer uses the IP address of a DNS resolver in the AWS US East region.
    :type ResolverIP: string
    :param EDNS0ClientSubnetIP: If the resolver that you specified for resolverip supports EDNS0, specify the IP address of a client in the applicable location.
    :type EDNS0ClientSubnetIP: string
    :param EDNS0ClientSubnetMask: If you specify an IP address for edns0clientsubnetip , you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify 192.0.2.44 for edns0clientsubnetip and 24 for edns0clientsubnetmask , the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits.
    :type EDNS0ClientSubnetMask: string
    """
    pass


def update_health_check(HealthCheckId=None, HealthCheckVersion=None, IPAddress=None, Port=None, ResourcePath=None,
                        FullyQualifiedDomainName=None, SearchString=None, FailureThreshold=None, Inverted=None,
                        HealthThreshold=None, ChildHealthChecks=None, EnableSNI=None, Regions=None,
                        AlarmIdentifier=None, InsufficientDataHealthStatus=None):
    """
    :param HealthCheckId: [REQUIRED]
            The ID for the health check for which you want detailed information. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.
            
    :type HealthCheckId: string
    :param HealthCheckVersion: A sequential counter that Amazon Route 53 sets to 1 when you create a health check and increments by 1 each time you update settings for the health check.
            We recommend that you use GetHealthCheck or ListHealthChecks to get the current value of HealthCheckVersion for the health check that you want to update, and that you include that value in your UpdateHealthCheck request. This prevents Amazon Route 53 from overwriting an intervening update:
            f the value in the UpdateHealthCheck request matches the value of HealthCheckVersion in the health check, Amazon Route 53 updates the health check with the new settings.
            If the value of HealthCheckVersion in the health check is greater, the health check was changed after you got the version number. Amazon Route 53 does not update the health check, and it returns a HealthCheckVersionMismatch error.
            
    :type HealthCheckVersion: integer
    :param IPAddress: The IPv4 IP address of the endpoint on which you want Amazon Route 53 to perform health checks. If you don't specify a value for IPAddress , Amazon Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IP address that DNS returns, Amazon Route 53 then checks the health of the endpoint.
            f the endpoint is an Amazon EC2 instance, we recommend that you create an Elastic IP address, associate it with your Amazon EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance never changes. For more information, see Elastic IP Addresses (EIP) in the Amazon EC2 User Guide for Linux Instances .
            Note
            If a health check already has a value for IPAddress , you can change the value. However, you can't update an existing health check to add or remove the value of IPAddress .
            For more information, see UpdateHealthCheckRequest$FullyQualifiedDomainName .
            
    :type IPAddress: string
    :param Port: The port on the endpoint on which you want Amazon Route 53 to perform health checks.
    :type Port: integer
    :param ResourcePath: The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html.
            Specify this value only if you want to change it.
            
    :type ResourcePath: string
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
            
    :type FullyQualifiedDomainName: string
    :param SearchString: If the value of Type is HTTP_STR_MATCH or HTTP_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Amazon Route 53 considers the resource healthy. (You can't change the value of Type when you update a health check.)
    :type SearchString: string
    :param FailureThreshold: The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
    :type FailureThreshold: integer
    :param Inverted: Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
    :type Inverted: boolean
    :param HealthThreshold: The number of child health checks that are associated with a CALCULATED health that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks and ChildHealthCheck elements.
            Note the following:
            If you specify a number greater than the number of child health checks, Amazon Route 53 always considers this health check to be unhealthy.
            If you specify 0 , Amazon Route 53 always considers this health check to be healthy.
            
    :type HealthThreshold: integer
    :param ChildHealthChecks: A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.
            (string) --
            
    :type ChildHealthChecks: list
    :param EnableSNI: Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
            Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don't enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
            The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.
            
    :type EnableSNI: boolean
    :param Regions: A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
            (string) --An Amazon EC2 region that you want Amazon Route 53 to use to perform health checks.
            
    :type Regions: list
    :param AlarmIdentifier: A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            Region (string) -- [REQUIRED]A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            For the current list of CloudWatch regions, see Amazon CloudWatch in AWS Regions and Endpoints in the Amazon Web Services General Reference .
            Name (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
            
    :type AlarmIdentifier: dict
    :param InsufficientDataHealthStatus: When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
            Healthy : Amazon Route 53 considers the health check to be healthy.
            Unhealthy : Amazon Route 53 considers the health check to be unhealthy.
            LastKnownStatus : Amazon Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
            
    :type InsufficientDataHealthStatus: string
    """
    pass


def update_hosted_zone_comment(Id=None, Comment=None):
    """
    :param Id: [REQUIRED]
            The ID for the hosted zone for which you want to update the comment.
            
    :type Id: string
    :param Comment: The new comment for the hosted zone. If you don't specify a value for Comment , Amazon Route 53 deletes the existing value of the Comment element, if any.
    :type Comment: string
    """
    pass


def update_traffic_policy_comment(Id=None, Version=None, Comment=None):
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
    pass


def update_traffic_policy_instance(Id=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
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
    pass
