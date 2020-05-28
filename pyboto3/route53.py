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

def associate_vpc_with_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    Associates an Amazon VPC with a private hosted zone.
    If you want to associate a VPC that was created by one AWS account with a private hosted zone that was created by a different account, do one of the following:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example associates the VPC with ID vpc-1a2b3c4d with the hosted zone with ID Z3M3LMPEXAMPLE.
    Expected Output:
    
    :example: response = client.associate_vpc_with_hosted_zone(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        },
        Comment='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the private hosted zone that you want to associate an Amazon VPC with.\nNote that you can\'t associate a VPC with a hosted zone that doesn\'t have an existing VPC association.\n

    :type VPC: dict
    :param VPC: [REQUIRED]\nA complex type that contains information about the VPC that you want to associate with a private hosted zone.\n\nVPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.\n\nVPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.\n\n\n

    :type Comment: string
    :param Comment: Optional: A comment about the association request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeInfo': {
        'Id': 'string',
        'Status': 'PENDING'|'INSYNC',
        'SubmittedAt': datetime(2015, 1, 1),
        'Comment': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information for the AssociateVPCWithHostedZone request.

ChangeInfo (dict) --
A complex type that describes the changes made to your hosted zone.

Id (string) --
The ID of the request.

Status (string) --
The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt (datetime) --
The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --
A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.









Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.NotAuthorizedException
Route53.Client.exceptions.InvalidVPCId
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.PublicZoneVPCAssociation
Route53.Client.exceptions.ConflictingDomainExists
Route53.Client.exceptions.LimitsExceeded

Examples
The following example associates the VPC with ID vpc-1a2b3c4d with the hosted zone with ID Z3M3LMPEXAMPLE.
response = client.associate_vpc_with_hosted_zone(
    Comment='',
    HostedZoneId='Z3M3LMPEXAMPLE',
    VPC={
        'VPCId': 'vpc-1a2b3c4d',
        'VPCRegion': 'us-east-2',
    },
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': '',
        'Id': '/change/C3HC6WDB2UANE2',
        'Status': 'INSYNC',
        'SubmittedAt': datetime(2017, 1, 31, 1, 36, 41, 1, 31, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    The ID of the private hosted zone that you want to associate an Amazon VPC with.
    Note that you can\'t associate a VPC with a hosted zone that doesn\'t have an existing VPC association.
    
    VPC (dict) -- [REQUIRED]
    A complex type that contains information about the VPC that you want to associate with a private hosted zone.
    
    VPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.
    
    VPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.
    
    
    
    Comment (string) -- Optional: A comment about the association request.
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def change_resource_record_sets(HostedZoneId=None, ChangeBatch=None):
    """
    Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use ChangeResourceRecordSets to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.
    To delete a resource record set, you must specify all the same values that you specified when you created it.
    The request body must include a document with a ChangeResourceRecordSetsRequest element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. Route 53 validates the changes in the request and then either makes all or none of the changes in the change batch request. This ensures that DNS routing isn\'t adversely affected by partial changes to the resource record sets in a hosted zone.
    For example, suppose a change batch request contains two changes: it deletes the CNAME resource record set for www.example.com and creates an alias resource record set for www.example.com. If validation for both records succeeds, Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If validation for either the DELETE or the CREATE action fails, then the request is canceled, and the original CNAME record continues to exist.
    To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isn\'t performing as expected. For more information, see Using Traffic Flow to Route DNS Traffic in the Amazon Route 53 Developer Guide .
    Use ChangeResourceRecordsSetsRequest to perform the following actions:
    The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax.
    For an example for each type of resource record set, see "Examples."
    Don\'t refer to the syntax in the "Parameter Syntax" section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using ChangeResourceRecordSets .
    When you submit a ChangeResourceRecordSets request, Route 53 propagates your changes to all of the Route 53 authoritative DNS servers. While your changes are propagating, GetChange returns a status of PENDING . When propagation is complete, GetChange returns a status of INSYNC . Changes generally propagate to all Route 53 name servers within 60 seconds. For more information, see GetChange .
    For information about the limits on a ChangeResourceRecordSets request, see Limits in the Amazon Route 53 Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a resource record set that routes Internet traffic to a resource with an IP address of 192.0.2.44.
    Expected Output:
    The following example creates two weighted resource record sets. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.
    Expected Output:
    The following example creates an alias resource record set that routes traffic to a CloudFront distribution.
    Expected Output:
    The following example creates two weighted alias resource record sets that route traffic to ELB load balancers. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.
    Expected Output:
    The following example creates two latency resource record sets that route traffic to EC2 instances. Traffic for example.com is routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.
    Expected Output:
    The following example creates two latency alias resource record sets that route traffic for example.com to ELB load balancers. Requests are routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.
    Expected Output:
    The following example creates primary and secondary failover resource record sets that route traffic to EC2 instances. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.
    Expected Output:
    The following example creates primary and secondary failover alias resource record sets that route traffic to ELB load balancers. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.
    Expected Output:
    The following example creates four geolocation resource record sets that use IPv4 addresses to route traffic to resources such as web servers running on EC2 instances. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).
    Expected Output:
    The following example creates four geolocation alias resource record sets that route traffic to ELB load balancers. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).
    Expected Output:
    
    :example: response = client.change_resource_record_sets(
        HostedZoneId='string',
        ChangeBatch={
            'Comment': 'string',
            'Changes': [
                {
                    'Action': 'CREATE'|'DELETE'|'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'string',
                        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                        'SetIdentifier': 'string',
                        'Weight': 123,
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-north-1'|'cn-northwest-1'|'ap-east-1'|'me-south-1'|'ap-south-1'|'af-south-1'|'eu-south-1',
                        'GeoLocation': {
                            'ContinentCode': 'string',
                            'CountryCode': 'string',
                            'SubdivisionCode': 'string'
                        },
                        'Failover': 'PRIMARY'|'SECONDARY',
                        'MultiValueAnswer': True|False,
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
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that contains the resource record sets that you want to change.\n

    :type ChangeBatch: dict
    :param ChangeBatch: [REQUIRED]\nA complex type that contains an optional comment and the Changes element.\n\nComment (string) --\nOptional: Any comments you want to include about a change batch request.\n\nChanges (list) -- [REQUIRED]Information about the changes to make to the record sets.\n\n(dict) --The information for each resource record set that you want to change.\n\nAction (string) -- [REQUIRED]The action to perform:\n\nCREATE : Creates a resource record set that has the specified values.\nDELETE : Deletes a existing resource record set.\n\n\nWarning\nTo delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use.\n\n\nUPSERT : If a resource record set doesn\'t already exist, Route 53 creates it. If a resource record set does exist, Route 53 updates it with the values in the request.\n\n\nResourceRecordSet (dict) -- [REQUIRED]Information about the resource record set to create, delete, or update.\n\nName (string) -- [REQUIRED]For ChangeResourceRecordSets requests, the name of the record that you want to create, update, or delete. For ListResourceRecordSets responses, the name of a record in the specified hosted zone.\n\nChangeResourceRecordSets Only\nEnter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.\nFor information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .\nYou can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, *.example.com . Note the following:\n\nThe * must replace the entire label. For example, you can\'t specify *prod.example.com or prod*.example.com .\nThe * can\'t replace any of the middle labels, for example, marketing.*.example.com.\nIf you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.\n\n\nWarning\nYou can\'t use the * wildcard for resource records sets that have a type of NS.\n\nYou can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You can\'t use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can\'t specify prod*.example.com .\n\nType (string) -- [REQUIRED]The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .\nValid values for basic resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT\nValues for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.\nValid values for multivalue answer resource record sets: A | AAAA | MX | NAPTR | PTR | SPF | SRV | TXT\n\nNote\nSPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, '...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.' In RFC 7208, see section 14.1, The SPF DNS Record Type .\n\nValues for alias resource record sets:\n\nAmazon API Gateway custom regional APIs and edge-optimized APIs: A\nCloudFront distributions: A  If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of A and one with a value of AAAA .\nAmazon API Gateway environment that has a regionalized subdomain : A\nELB load balancers: A | AAAA\nAmazon S3 buckets: A\nAmazon Virtual Private Cloud interface VPC endpoints A\nAnother resource record set in this hosted zone: Specify the type of the resource record set that you\'re creating the alias for. All values are supported except NS and SOA .\n\n\nNote\nIf you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t route traffic to a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.\n\n\nSetIdentifier (string) --\nResource record sets that have a routing policy other than simple: An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of SetIdentifier must be unique for each resource record set.\nFor information about routing policies, see Choosing a Routing Policy in the Amazon Route 53 Developer Guide .\n\nWeight (integer) --\nWeighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource\'s weight to the total. Note the following:\n\nYou must specify a value for the Weight element for every weighted resource record set.\nYou can only specify one ResourceRecord per weighted resource record set.\nYou can\'t create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.\nYou can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.\nFor weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .\n\n\nRegion (string) --\nLatency-based resource record sets only: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.\n\nNote\nAlthough creating latency and latency alias resource record sets in a private hosted zone is allowed, it\'s not supported.\n\nWhen Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.\nNote the following:\n\nYou can only specify one ResourceRecord per latency resource record set.\nYou can only create one latency resource record set for each Amazon EC2 Region.\nYou aren\'t required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.\nYou can\'t create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.\n\n\nGeoLocation (dict) --\nGeolocation resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .\n\nNote\nAlthough creating geolocation and geolocation alias resource record sets in a private hosted zone is allowed, it\'s not supported.\n\nIf you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.\nYou can\'t create two geolocation resource record sets that specify the same geographic location.\nThe value * in the CountryCode element matches all geographic locations that aren\'t specified in other geolocation resource record sets that have the same values for the Name and Type elements.\n\nWarning\nGeolocation works by mapping IP addresses to locations. However, some IP addresses aren\'t mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can\'t identify. We recommend that you create a resource record set for which the value of CountryCode is * . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven\'t created geolocation resource record sets and queries from IP addresses that aren\'t mapped to a location. If you don\'t create a * resource record set, Route 53 returns a 'no answer' response for queries from those locations.\n\nYou can\'t create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.\n\nContinentCode (string) --The two-letter code for the continent.\nAmazon Route 53 supports the following continent codes:\n\nAF : Africa\nAN : Antarctica\nAS : Asia\nEU : Europe\nOC : Oceania\nNA : North America\nSA : South America\n\nConstraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.\n\nCountryCode (string) --For geolocation resource record sets, the two-letter code for a country.\nAmazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .\n\nSubdivisionCode (string) --For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn\'t support any other values for SubdivisionCode . For a list of state abbreviations, see Appendix B: Two\xe2\x80\x93Letter State and Possession Abbreviations on the United States Postal Service website.\nIf you specify subdivisioncode , you must also specify US for CountryCode .\n\n\n\nFailover (string) --\nFailover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.\nExcept where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:\n\nWhen the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.\nWhen the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.\nWhen the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.\nIf you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.\n\nYou can\'t create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.\nFor failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.\nFor more information about configuring failover for Route 53, see the following topics in the Amazon Route 53 Developer Guide :\n\nRoute 53 Health Checks and DNS Failover\nConfiguring Failover in a Private Hosted Zone\n\n\nMultiValueAnswer (boolean) --\nMultivalue answer resource record sets only : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify true for MultiValueAnswer . Note the following:\n\nIf you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.\nIf you don\'t associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.\nRoute 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.\nIf you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.\nWhen all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.\nIf a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.\n\nYou can\'t create multivalue answer alias records.\n\nTTL (integer) --The resource record cache time to live (TTL), in seconds. Note the following:\n\nIf you\'re creating or updating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.\nIf you\'re associating this resource record set with a health check (if you\'re adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.\nAll of the resource record sets in a group of weighted resource record sets must have the same value for TTL .\nIf a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .\n\n\nResourceRecords (list) --Information about the resource records to act upon.\n\nNote\nIf you\'re creating an alias resource record set, omit ResourceRecords .\n\n\n(dict) --Information specific to the resource record.\n\nNote\nIf you\'re creating an alias resource record set, omit ResourceRecord .\n\n\nValue (string) -- [REQUIRED]The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .\nYou can specify more than one value for all record types except CNAME and SOA .\n\nNote\nIf you\'re creating an alias resource record set, omit Value .\n\n\n\n\n\n\nAliasTarget (dict) --\nAlias resource record sets only: Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.\nIf you\'re creating resource records sets for a private hosted zone, note the following:\n\nYou can\'t create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.\nCreating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.\nFor information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .\n\n\nHostedZoneId (string) -- [REQUIRED]\nAlias resource records sets only : The value used depends on where you want to route traffic:\nAmazon API Gateway custom regional APIs and edge-optimized APIs\n\nSpecify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command get-domain-names :\n\nFor regional APIs, specify the value of regionalHostedZoneId .\nFor edge-optimized APIs, specify the value of distributionHostedZoneId .Amazon Virtual Private Cloud interface VPC endpoint\n\n\nSpecify the hosted zone ID for your interface endpoint. You can get the value of HostedZoneId using the AWS CLI command describe-vpc-endpoints .\n\nCloudFront distribution\nSpecify Z2FDTNDATAQYW2 .\n\nNote\nAlias resource record sets for CloudFront can\'t be created in a private zone.\nElastic Beanstalk environment\n\nSpecify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see AWS Elastic Beanstalk in the 'AWS Service Endpoints' chapter of the Amazon Web Services General Reference .\n\nELB load balancer\nSpecify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:\n\nService Endpoints table in the 'Elastic Load Balancing Endpoints and Quotas' topic in the Amazon Web Services General Reference : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.\nAWS Management Console : Go to the Amazon EC2 page, choose Load Balancers in the navigation pane, select the load balancer, and get the value of the Hosted zone field on the Description tab.\nElastic Load Balancing API : Use DescribeLoadBalancers to get the applicable value. For more information, see the applicable guide:\nClassic Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneNameId .\nApplication and Network Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneId .\n\n\nAWS CLI : Use describe-load-balancers to get the applicable value. For more information, see the applicable guide:\nClassic Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneNameId .\nApplication and Network Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneId .\n\nAWS Global Accelerator accelerator\n\n\nSpecify Z2BJ6XQ5FK7U4H .\n\nAn Amazon S3 bucket configured as a static website\nSpecify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference .\n\nAnother Route 53 resource record set in your hosted zone\nSpecify the hosted zone ID of your hosted zone. (An alias resource record set can\'t reference a resource record set in a different hosted zone.)\n\nDNSName (string) -- [REQUIRED]\nAlias resource record sets only: The value that you specify depends on where you want to route queries:\nAmazon API Gateway custom regional APIs and edge-optimized APIs\n\nSpecify the applicable domain name for your API. You can get the applicable value using the AWS CLI command get-domain-names :\n\nFor regional APIs, specify the value of regionalDomainName .\nFor edge-optimized APIs, specify the value of distributionDomainName . This is the name of the associated CloudFront distribution, such as da1b2c3d4e5.cloudfront.net .\n\n\nNote\nThe name of the record that you\'re creating must match a custom domain name for your API, such as api.example.com .\nAmazon Virtual Private Cloud interface VPC endpoint\n\nEnter the API endpoint for the interface endpoint, such as vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of DnsName using the AWS CLI command describe-vpc-endpoints .\n\nCloudFront distribution\nSpecify the domain name that CloudFront assigned when you created your distribution.\nYour CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .\nYou can\'t create a resource record set in a private hosted zone to route traffic to a CloudFront distribution.\n\nNote\nFor failover alias records, you can\'t specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can\'t include the same alternate domain name in more than one distribution.\nElastic Beanstalk environment\n\nIf the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name my-environment.*us-west-2* .elasticbeanstalk.com is a regionalized domain name.\n\nWarning\nFor environments that were created before early 2016, the domain name doesn\'t include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can\'t create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can\'t create a record that routes traffic for example.com to your Elastic Beanstalk environment.\n\nFor Elastic Beanstalk environments that have regionalized subdomains, specify the CNAME attribute for the environment. You can use the following methods to get the value of the CNAME attribute:\n\nAWS Management Console : For information about how to get the value by using the console, see Using Custom Domains with AWS Elastic Beanstalk in the AWS Elastic Beanstalk Developer Guide .\nElastic Beanstalk API : Use the DescribeEnvironments action to get the value of the CNAME attribute. For more information, see DescribeEnvironments in the AWS Elastic Beanstalk API Reference .\nAWS CLI : Use the describe-environments command to get the value of the CNAME attribute. For more information, see describe-environments in the AWS CLI Command Reference .ELB load balancer\n\n\nSpecify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI.\n\nAWS Management Console : Go to the EC2 page, choose Load Balancers in the navigation pane, choose the load balancer, choose the Description tab, and get the value of the DNS name field. If you\'re routing traffic to a Classic Load Balancer, get the value that begins with dualstack . If you\'re routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.\nElastic Load Balancing API : Use DescribeLoadBalancers to get the value of DNSName . For more information, see the applicable guide:\nClassic Load Balancers: DescribeLoadBalancers\nApplication and Network Load Balancers: DescribeLoadBalancers\n\n\nAWS CLI : Use describe-load-balancers to get the value of DNSName . For more information, see the applicable guide:\nClassic Load Balancers: describe-load-balancers\nApplication and Network Load Balancers: describe-load-balancers\n\nAWS Global Accelerator accelerator\n\n\nSpecify the DNS name for your accelerator:\n\nGlobal Accelerator API: To get the DNS name, use DescribeAccelerator .\nAWS CLI: To get the DNS name, use describe-accelerator .Amazon S3 bucket that is configured as a static website\n\n\nSpecify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, s3-website.us-east-2.amazonaws.com . For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference . For more information about using S3 buckets for websites, see Getting Started with Amazon Route 53 in the Amazon Route 53 Developer Guide.\n\nAnother Route 53 resource record set\nSpecify the value of the Name element for a resource record set in the current hosted zone.\n\nNote\nIf you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t specify the domain name for a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record that you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.\n\n\nEvaluateTargetHealth (boolean) -- [REQUIRED]\nApplies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets: When EvaluateTargetHealth is true , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone.\nNote the following:\n\nCloudFront distributions\nYou can\'t set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.\n\nElastic Beanstalk environments that have regionalized subdomains\nIf you specify an Elastic Beanstalk environment in DNSName and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set EvaluateTargetHealth to true and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.\nIf the environment contains a single Amazon EC2 instance, there are no special requirements.\n\nELB load balancers\nHealth checking behavior depends on the type of load balancer:\n\nClassic Load Balancers : If you specify an ELB Classic Load Balancer in DNSName , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set EvaluateTargetHealth to true and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.\nApplication and Network Load Balancers : If you specify an ELB Application or Network Load Balancer and you set EvaluateTargetHealth to true , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:\nFor an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.\nA target group that has no registered targets is considered unhealthy.\n\n\n\n\nNote\nWhen you create a load balancer, you configure settings for Elastic Load Balancing health checks; they\'re not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.\nS3 buckets\n\nThere are no special requirements for setting EvaluateTargetHealth to true when the alias target is an S3 bucket.\n\nOther records in the same hosted zone\nIf the AWS resource that you specify in DNSName is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see What Happens When You Omit Health Checks? in the Amazon Route 53 Developer Guide .\nFor more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .\n\n\n\nHealthCheckId (string) --If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the HealthCheckId element and specify the ID of the applicable health check.\nRoute 53 determines whether a resource record set is healthy based on one of the following:\n\nBy periodically sending a request to the endpoint that is specified in the health check\nBy aggregating the status of a specified group of health checks (calculated health checks)\nBy determining the current state of a CloudWatch alarm (CloudWatch metric health checks)\n\n\nWarning\nRoute 53 doesn\'t check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.\n\nFor more information, see the following topics in the Amazon Route 53 Developer Guide :\n\nHow Amazon Route 53 Determines Whether an Endpoint Is Healthy\nRoute 53 Health Checks and DNS Failover\nConfiguring Failover in a Private Hosted Zone\n\n\nWhen to Specify HealthCheckId\nSpecifying a value for HealthCheckId is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:\n\nNon-alias resource record sets : You\'re checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets. If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.\nAlias resource record sets : You specify the following settings:\nYou set EvaluateTargetHealth to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).\nYou configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.\nYou specify a health check ID for the non-alias resource record set.\n\n\n\nIf the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.\nIf the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.\n\nNote\n\nThe alias resource record set can also route traffic to a group of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.\nGeolocation Routing\n\nFor geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has * for CountryCode is * , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:\n\nThe United States\nNorth America\nThe default resource record set\n\n\nSpecifying the Health Check Endpoint by Domain Name\nIf your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com . For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com ), not the name of the resource record sets (www.example.com ).\n\nWarning\nHealth check results will be unpredictable if you do the following:\n\nCreate a health check that has the same value for FullyQualifiedDomainName as the name of a resource record set.\nAssociate that health check with the resource record set.\n\n\n\nTrafficPolicyInstanceId (string) --When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Route 53 created this resource record set for.\n\nWarning\nTo delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use.\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeInfo': {
        'Id': 'string',
        'Status': 'PENDING'|'INSYNC',
        'SubmittedAt': datetime(2015, 1, 1),
        'Comment': 'string'
    }
}


Response Structure

(dict) --
A complex type containing the response for the request.

ChangeInfo (dict) --
A complex type that contains information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.

Id (string) --
The ID of the request.

Status (string) --
The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt (datetime) --
The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --
A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.









Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.InvalidChangeBatch
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.PriorRequestNotComplete

Examples
The following example creates a resource record set that routes Internet traffic to a resource with an IP address of 192.0.2.44.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
                        },
                    ],
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Web server for example.com',
    },
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Web server for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates two weighted resource record sets. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba',
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
                        },
                    ],
                    'SetIdentifier': 'Seattle data center',
                    'TTL': 60,
                    'Type': 'A',
                    'Weight': 100,
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba',
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.45',
                        },
                    ],
                    'SetIdentifier': 'Portland data center',
                    'TTL': 60,
                    'Type': 'A',
                    'Weight': 200,
                },
            },
        ],
        'Comment': 'Web servers for example.com',
    },
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Web servers for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates an alias resource record set that routes traffic to a CloudFront distribution.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'd123rk29d0stfj.cloudfront.net',
                        'EvaluateTargetHealth': False,
                        'HostedZoneId': 'Z2FDTNDATAQYW2',
                    },
                    'Name': 'example.com',
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'CloudFront distribution for example.com',
    },
    # Depends on the type of resource that you want to route traffic to
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'CloudFront distribution for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates two weighted alias resource record sets that route traffic to ELB load balancers. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z3AADJGX6KTTL2',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'Ohio region',
                    'Type': 'A',
                    'Weight': 100,
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z1H1FL5HABSF5',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'Oregon region',
                    'Type': 'A',
                    'Weight': 200,
                },
            },
        ],
        'Comment': 'ELB load balancers for example.com',
    },
    # Depends on the type of resource that you want to route traffic to
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'ELB load balancers for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates two latency resource record sets that route traffic to EC2 instances. Traffic for example.com is routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba',
                    'Name': 'example.com',
                    'Region': 'us-east-2',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
                        },
                    ],
                    'SetIdentifier': 'Ohio region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba',
                    'Name': 'example.com',
                    'Region': 'us-west-2',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.45',
                        },
                    ],
                    'SetIdentifier': 'Oregon region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'EC2 instances for example.com',
    },
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'EC2 instances for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates two latency alias resource record sets that route traffic for example.com to ELB load balancers. Requests are routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z3AADJGX6KTTL2',
                    },
                    'Name': 'example.com',
                    'Region': 'us-east-2',
                    'SetIdentifier': 'Ohio region',
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z1H1FL5HABSF5',
                    },
                    'Name': 'example.com',
                    'Region': 'us-west-2',
                    'SetIdentifier': 'Oregon region',
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'ELB load balancers for example.com',
    },
    # Depends on the type of resource that you want to route traffic to
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'ELB load balancers for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates primary and secondary failover resource record sets that route traffic to EC2 instances. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Failover': 'PRIMARY',
                    'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba',
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
                        },
                    ],
                    'SetIdentifier': 'Ohio region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Failover': 'SECONDARY',
                    'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba',
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.45',
                        },
                    ],
                    'SetIdentifier': 'Oregon region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Failover configuration for example.com',
    },
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Failover configuration for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates primary and secondary failover alias resource record sets that route traffic to ELB load balancers. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z3AADJGX6KTTL2',
                    },
                    'Failover': 'PRIMARY',
                    'Name': 'example.com',
                    'SetIdentifier': 'Ohio region',
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z1H1FL5HABSF5',
                    },
                    'Failover': 'SECONDARY',
                    'Name': 'example.com',
                    'SetIdentifier': 'Oregon region',
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Failover alias configuration for example.com',
    },
    # Depends on the type of resource that you want to route traffic to
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Failover alias configuration for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates four geolocation resource record sets that use IPv4 addresses to route traffic to resources such as web servers running on EC2 instances. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'NA',
                    },
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.44',
                        },
                    ],
                    'SetIdentifier': 'North America',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'SA',
                    },
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.45',
                        },
                    ],
                    'SetIdentifier': 'South America',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'EU',
                    },
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.46',
                        },
                    ],
                    'SetIdentifier': 'Europe',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'CountryCode': '*',
                    },
                    'Name': 'example.com',
                    'ResourceRecords': [
                        {
                            'Value': '192.0.2.47',
                        },
                    ],
                    'SetIdentifier': 'Other locations',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Geolocation configuration for example.com',
    },
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Geolocation configuration for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates four geolocation alias resource record sets that route traffic to ELB load balancers. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z3AADJGX6KTTL2',
                    },
                    'GeoLocation': {
                        'ContinentCode': 'NA',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'North America',
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-234567890.sa-east-1.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z2P70J7HTTTPLU',
                    },
                    'GeoLocation': {
                        'ContinentCode': 'SA',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'South America',
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-234567890.eu-central-1.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z215JYRZR1TBD5',
                    },
                    'GeoLocation': {
                        'ContinentCode': 'EU',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'Europe',
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'AliasTarget': {
                        'DNSName': 'example-com-234567890.ap-southeast-1.elb.amazonaws.com ',
                        'EvaluateTargetHealth': True,
                        'HostedZoneId': 'Z1LMS91P8CMLE5',
                    },
                    'GeoLocation': {
                        'CountryCode': '*',
                    },
                    'Name': 'example.com',
                    'SetIdentifier': 'Other locations',
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Geolocation alias configuration for example.com',
    },
    # Depends on the type of resource that you want to route traffic to
    HostedZoneId='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'ChangeInfo': {
        'Comment': 'Geolocation alias configuration for example.com',
        'Id': '/change/C2682N5HXP0BZ4',
        'Status': 'PENDING',
        'SubmittedAt': datetime(2017, 2, 10, 1, 36, 41, 4, 41, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    DELETE : Deletes a existing resource record set.
    
    
    Warning
    To delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use.
    
    
    UPSERT : If a resource record set doesn\'t already exist, Route 53 creates it. If a resource record set does exist, Route 53 updates it with the values in the request.
    
    
    ResourceRecordSet (dict) -- [REQUIRED]Information about the resource record set to create, delete, or update.
    
    Name (string) -- [REQUIRED]For ChangeResourceRecordSets requests, the name of the record that you want to create, update, or delete. For ListResourceRecordSets responses, the name of a record in the specified hosted zone.
    
    ChangeResourceRecordSets Only
    Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
    For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
    You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, *.example.com . Note the following:
    
    The * must replace the entire label. For example, you can\'t specify *prod.example.com or prod*.example.com .
    The * can\'t replace any of the middle labels, for example, marketing.*.example.com.
    If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
    
    
    Warning
    You can\'t use the * wildcard for resource records sets that have a type of NS.
    
    You can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You can\'t use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can\'t specify prod*.example.com .
    
    Type (string) -- [REQUIRED]The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
    Valid values for basic resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
    Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
    Valid values for multivalue answer resource record sets: A | AAAA | MX | NAPTR | PTR | SPF | SRV | TXT
    
    Note
    SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, The SPF DNS Record Type .
    
    Values for alias resource record sets:
    
    Amazon API Gateway custom regional APIs and edge-optimized APIs: A
    CloudFront distributions: A   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of A and one with a value of AAAA .
    Amazon API Gateway environment that has a regionalized subdomain : A
    ELB load balancers: A | AAAA
    Amazon S3 buckets: A
    Amazon Virtual Private Cloud interface VPC endpoints A
    Another resource record set in this hosted zone: Specify the type of the resource record set that you\'re creating the alias for. All values are supported except NS and SOA .
    
    
    Note
    If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t route traffic to a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.
    
    
    SetIdentifier (string) --
    Resource record sets that have a routing policy other than simple: An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of SetIdentifier must be unique for each resource record set.
    For information about routing policies, see Choosing a Routing Policy in the Amazon Route 53 Developer Guide .
    
    Weight (integer) --
    Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource\'s weight to the total. Note the following:
    
    You must specify a value for the Weight element for every weighted resource record set.
    You can only specify one ResourceRecord per weighted resource record set.
    You can\'t create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
    You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
    For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .
    
    
    Region (string) --
    Latency-based resource record sets only: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
    
    Note
    Although creating latency and latency alias resource record sets in a private hosted zone is allowed, it\'s not supported.
    
    When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.
    Note the following:
    
    You can only specify one ResourceRecord per latency resource record set.
    You can only create one latency resource record set for each Amazon EC2 Region.
    You aren\'t required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.
    You can\'t create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.
    
    
    GeoLocation (dict) --
    Geolocation resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .
    
    Note
    Although creating geolocation and geolocation alias resource record sets in a private hosted zone is allowed, it\'s not supported.
    
    If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
    You can\'t create two geolocation resource record sets that specify the same geographic location.
    The value * in the CountryCode element matches all geographic locations that aren\'t specified in other geolocation resource record sets that have the same values for the Name and Type elements.
    
    Warning
    Geolocation works by mapping IP addresses to locations. However, some IP addresses aren\'t mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can\'t identify. We recommend that you create a resource record set for which the value of CountryCode is * . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven\'t created geolocation resource record sets and queries from IP addresses that aren\'t mapped to a location. If you don\'t create a * resource record set, Route 53 returns a "no answer" response for queries from those locations.
    
    You can\'t create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.
    
    ContinentCode (string) --The two-letter code for the continent.
    Amazon Route 53 supports the following continent codes:
    
    AF : Africa
    AN : Antarctica
    AS : Asia
    EU : Europe
    OC : Oceania
    NA : North America
    SA : South America
    
    Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.
    
    CountryCode (string) --For geolocation resource record sets, the two-letter code for a country.
    Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .
    
    SubdivisionCode (string) --For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn\'t support any other values for SubdivisionCode . For a list of state abbreviations, see Appendix B: Two\xe2\x80\x93Letter State and Possession Abbreviations on the United States Postal Service website.
    If you specify subdivisioncode , you must also specify US for CountryCode .
    
    
    
    Failover (string) --
    Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
    Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:
    
    When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
    When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
    When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
    If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.
    
    You can\'t create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
    For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
    For more information about configuring failover for Route 53, see the following topics in the Amazon Route 53 Developer Guide :
    
    Route 53 Health Checks and DNS Failover
    Configuring Failover in a Private Hosted Zone
    
    
    MultiValueAnswer (boolean) --
    Multivalue answer resource record sets only : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify true for MultiValueAnswer . Note the following:
    
    If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.
    If you don\'t associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.
    Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.
    If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.
    When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.
    If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.
    
    You can\'t create multivalue answer alias records.
    
    TTL (integer) --The resource record cache time to live (TTL), in seconds. Note the following:
    
    If you\'re creating or updating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
    If you\'re associating this resource record set with a health check (if you\'re adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
    All of the resource record sets in a group of weighted resource record sets must have the same value for TTL .
    If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .
    
    
    ResourceRecords (list) --Information about the resource records to act upon.
    
    Note
    If you\'re creating an alias resource record set, omit ResourceRecords .
    
    
    (dict) --Information specific to the resource record.
    
    Note
    If you\'re creating an alias resource record set, omit ResourceRecord .
    
    
    Value (string) -- [REQUIRED]The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
    You can specify more than one value for all record types except CNAME and SOA .
    
    Note
    If you\'re creating an alias resource record set, omit Value .
    
    
    
    
    
    
    AliasTarget (dict) --
    Alias resource record sets only: Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.
    If you\'re creating resource records sets for a private hosted zone, note the following:
    
    You can\'t create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.
    Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.
    For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .
    
    
    HostedZoneId (string) -- [REQUIRED]
    Alias resource records sets only : The value used depends on where you want to route traffic:
    Amazon API Gateway custom regional APIs and edge-optimized APIs
    
    Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command get-domain-names :
    
    For regional APIs, specify the value of regionalHostedZoneId .
    For edge-optimized APIs, specify the value of distributionHostedZoneId .Amazon Virtual Private Cloud interface VPC endpoint
    
    
    Specify the hosted zone ID for your interface endpoint. You can get the value of HostedZoneId using the AWS CLI command describe-vpc-endpoints .
    
    CloudFront distribution
    Specify Z2FDTNDATAQYW2 .
    
    Note
    Alias resource record sets for CloudFront can\'t be created in a private zone.
    Elastic Beanstalk environment
    
    Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see AWS Elastic Beanstalk in the "AWS Service Endpoints" chapter of the Amazon Web Services General Reference .
    
    ELB load balancer
    Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
    
    Service Endpoints table in the "Elastic Load Balancing Endpoints and Quotas" topic in the Amazon Web Services General Reference : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.
    AWS Management Console : Go to the Amazon EC2 page, choose Load Balancers in the navigation pane, select the load balancer, and get the value of the Hosted zone field on the Description tab.
    Elastic Load Balancing API : Use DescribeLoadBalancers to get the applicable value. For more information, see the applicable guide:
    Classic Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneNameId .
    Application and Network Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneId .
    
    
    AWS CLI : Use describe-load-balancers to get the applicable value. For more information, see the applicable guide:
    Classic Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneNameId .
    Application and Network Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneId .
    
    AWS Global Accelerator accelerator
    
    
    Specify Z2BJ6XQ5FK7U4H .
    
    An Amazon S3 bucket configured as a static website
    Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference .
    
    Another Route 53 resource record set in your hosted zone
    Specify the hosted zone ID of your hosted zone. (An alias resource record set can\'t reference a resource record set in a different hosted zone.)
    
    DNSName (string) -- [REQUIRED]
    Alias resource record sets only: The value that you specify depends on where you want to route queries:
    Amazon API Gateway custom regional APIs and edge-optimized APIs
    
    Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command get-domain-names :
    
    For regional APIs, specify the value of regionalDomainName .
    For edge-optimized APIs, specify the value of distributionDomainName . This is the name of the associated CloudFront distribution, such as da1b2c3d4e5.cloudfront.net .
    
    
    Note
    The name of the record that you\'re creating must match a custom domain name for your API, such as api.example.com .
    Amazon Virtual Private Cloud interface VPC endpoint
    
    Enter the API endpoint for the interface endpoint, such as vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of DnsName using the AWS CLI command describe-vpc-endpoints .
    
    CloudFront distribution
    Specify the domain name that CloudFront assigned when you created your distribution.
    Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
    You can\'t create a resource record set in a private hosted zone to route traffic to a CloudFront distribution.
    
    Note
    For failover alias records, you can\'t specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can\'t include the same alternate domain name in more than one distribution.
    Elastic Beanstalk environment
    
    If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name my-environment.*us-west-2* .elasticbeanstalk.com is a regionalized domain name.
    
    Warning
    For environments that were created before early 2016, the domain name doesn\'t include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can\'t create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can\'t create a record that routes traffic for example.com to your Elastic Beanstalk environment.
    
    For Elastic Beanstalk environments that have regionalized subdomains, specify the CNAME attribute for the environment. You can use the following methods to get the value of the CNAME attribute:
    
    AWS Management Console : For information about how to get the value by using the console, see Using Custom Domains with AWS Elastic Beanstalk in the AWS Elastic Beanstalk Developer Guide .
    Elastic Beanstalk API : Use the DescribeEnvironments action to get the value of the CNAME attribute. For more information, see DescribeEnvironments in the AWS Elastic Beanstalk API Reference .
    AWS CLI : Use the describe-environments command to get the value of the CNAME attribute. For more information, see describe-environments in the AWS CLI Command Reference .ELB load balancer
    
    
    Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI.
    
    AWS Management Console : Go to the EC2 page, choose Load Balancers in the navigation pane, choose the load balancer, choose the Description tab, and get the value of the DNS name field.  If you\'re routing traffic to a Classic Load Balancer, get the value that begins with dualstack . If you\'re routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.
    Elastic Load Balancing API : Use DescribeLoadBalancers to get the value of DNSName . For more information, see the applicable guide:
    Classic Load Balancers: DescribeLoadBalancers
    Application and Network Load Balancers: DescribeLoadBalancers
    
    
    AWS CLI : Use describe-load-balancers to get the value of DNSName . For more information, see the applicable guide:
    Classic Load Balancers: describe-load-balancers
    Application and Network Load Balancers: describe-load-balancers
    
    AWS Global Accelerator accelerator
    
    
    Specify the DNS name for your accelerator:
    
    Global Accelerator API: To get the DNS name, use DescribeAccelerator .
    AWS CLI: To get the DNS name, use describe-accelerator .Amazon S3 bucket that is configured as a static website
    
    
    Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, s3-website.us-east-2.amazonaws.com . For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference . For more information about using S3 buckets for websites, see Getting Started with Amazon Route 53 in the Amazon Route 53 Developer Guide.
    
    Another Route 53 resource record set
    Specify the value of the Name element for a resource record set in the current hosted zone.
    
    Note
    If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t specify the domain name for a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record that you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.
    
    
    EvaluateTargetHealth (boolean) -- [REQUIRED]
    Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets: When EvaluateTargetHealth is true , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone.
    Note the following:
    
    CloudFront distributions
    You can\'t set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.
    
    Elastic Beanstalk environments that have regionalized subdomains
    If you specify an Elastic Beanstalk environment in DNSName and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set EvaluateTargetHealth to true and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.
    If the environment contains a single Amazon EC2 instance, there are no special requirements.
    
    ELB load balancers
    Health checking behavior depends on the type of load balancer:
    
    Classic Load Balancers : If you specify an ELB Classic Load Balancer in DNSName , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set EvaluateTargetHealth to true and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.
    Application and Network Load Balancers : If you specify an ELB Application or Network Load Balancer and you set EvaluateTargetHealth to true , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:
    For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.
    A target group that has no registered targets is considered unhealthy.
    
    
    
    
    Note
    When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they\'re not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.
    S3 buckets
    
    There are no special requirements for setting EvaluateTargetHealth to true when the alias target is an S3 bucket.
    
    Other records in the same hosted zone
    If the AWS resource that you specify in DNSName is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see What Happens When You Omit Health Checks? in the Amazon Route 53 Developer Guide .
    For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .
    
    
    
    HealthCheckId (string) --If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the HealthCheckId element and specify the ID of the applicable health check.
    Route 53 determines whether a resource record set is healthy based on one of the following:
    
    By periodically sending a request to the endpoint that is specified in the health check
    By aggregating the status of a specified group of health checks (calculated health checks)
    By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)
    
    
    Warning
    Route 53 doesn\'t check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.
    
    For more information, see the following topics in the Amazon Route 53 Developer Guide :
    
    How Amazon Route 53 Determines Whether an Endpoint Is Healthy
    Route 53 Health Checks and DNS Failover
    Configuring Failover in a Private Hosted Zone
    
    
    When to Specify HealthCheckId
    Specifying a value for HealthCheckId is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:
    
    Non-alias resource record sets : You\'re checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.  If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.
    Alias resource record sets : You specify the following settings:
    You set EvaluateTargetHealth to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).
    You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.
    You specify a health check ID for the non-alias resource record set.
    
    
    
    If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.
    If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.
    
    Note
    
    The alias resource record set can also route traffic to a group of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.
    Geolocation Routing
    
    For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has * for CountryCode is * , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:
    
    The United States
    North America
    The default resource record set
    
    
    Specifying the Health Check Endpoint by Domain Name
    If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com . For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com ), not the name of the resource record sets (www.example.com ).
    
    Warning
    Health check results will be unpredictable if you do the following:
    
    Create a health check that has the same value for FullyQualifiedDomainName as the name of a resource record set.
    Associate that health check with the resource record set.
    
    
    
    TrafficPolicyInstanceId (string) --When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Route 53 created this resource record set for.
    
    Warning
    To delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use.
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def change_tags_for_resource(ResourceType=None, ResourceId=None, AddTags=None, RemoveTagKeys=None):
    """
    Adds, edits, or deletes tags for a health check or a hosted zone.
    For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example adds two tags and removes one tag from the hosted zone with ID Z3M3LMPEXAMPLE.
    Expected Output:
    
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
    :param ResourceType: [REQUIRED]\nThe type of the resource.\n\nThe resource type for health checks is healthcheck .\nThe resource type for hosted zones is hostedzone .\n\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource for which you want to add, change, or delete tags.\n

    :type AddTags: list
    :param AddTags: A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags that you want to edit Value for.\nYou can add a maximum of 10 tags to a health check or a hosted zone.\n\n(dict) --A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.\n\nKey (string) --The value of Key depends on the operation that you want to perform:\n\nAdd a tag to a health check or hosted zone : Key is the name that you want to give the new tag.\nEdit a tag : Key is the name of the tag that you want to change the Value for.\nDelete a key : Key is the name of the tag you want to remove.\nGive a name to a health check : Edit the default Name tag. In the Amazon Route 53 console, the list of your health checks includes a Name column that lets you see the name that you\'ve given to each health check.\n\n\nValue (string) --The value of Value depends on the operation that you want to perform:\n\nAdd a tag to a health check or hosted zone : Value is the value that you want to give the new tag.\nEdit a tag : Value is the new value that you want to assign the tag.\n\n\n\n\n\n

    :type RemoveTagKeys: list
    :param RemoveTagKeys: A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Empty response for the request.





Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.PriorRequestNotComplete
Route53.Client.exceptions.ThrottlingException

Examples
The following example adds two tags and removes one tag from the hosted zone with ID Z3M3LMPEXAMPLE.
response = client.change_tags_for_resource(
    AddTags=[
        {
            'Key': 'apex',
            'Value': '3874',
        },
        {
            'Key': 'acme',
            'Value': '4938',
        },
    ],
    RemoveTagKeys=[
        'Nadir',
    ],
    ResourceId='Z3M3LMPEXAMPLE',
    # Valid values are healthcheck and hostedzone.
    ResourceType='hostedzone',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchHealthCheck
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.PriorRequestNotComplete
    Route53.Client.exceptions.ThrottlingException
    
    """
    pass

def create_health_check(CallerReference=None, HealthCheckConfig=None):
    """
    Creates a new health check.
    For information about adding health checks to resource record sets, see HealthCheckId in ChangeResourceRecordSets .
    If you\'re registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.
    You can associate health checks with failover resource record sets in a private hosted zone. Note the following:
    See also: AWS API Documentation
    
    Exceptions
    
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
            'Disabled': True|False,
            'HealthThreshold': 123,
            'ChildHealthChecks': [
                'string',
            ],
            'EnableSNI': True|False,
            'Regions': [
                'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
            ],
            'AlarmIdentifier': {
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
                'Name': 'string'
            },
            'InsufficientDataHealthStatus': 'Healthy'|'Unhealthy'|'LastKnownStatus'
        }
    )
    
    
    :type CallerReference: string
    :param CallerReference: [REQUIRED]\nA unique string that identifies the request and that allows you to retry a failed CreateHealthCheck request without the risk of creating two identical health checks:\n\nIf you send a CreateHealthCheck request with the same CallerReference and settings as a previous request, and if the health check doesn\'t exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the settings for the existing health check.\nIf you send a CreateHealthCheck request with the same CallerReference as a deleted health check, regardless of the settings, Route 53 returns a HealthCheckAlreadyExists error.\nIf you send a CreateHealthCheck request with the same CallerReference as an existing health check but with different settings, Route 53 returns a HealthCheckAlreadyExists error.\nIf you send a CreateHealthCheck request with a unique CallerReference but settings identical to an existing health check, Route 53 creates the health check.\n\n

    :type HealthCheckConfig: dict
    :param HealthCheckConfig: [REQUIRED]\nA complex type that contains settings for a new health check.\n\nIPAddress (string) --The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.\nUse one of the following formats for the value of IPAddress :\n\nIPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .\nIPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .\n\nIf the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.\nFor more information, see FullyQualifiedDomainName .\nConstraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:\n\nRFC 5735, Special Use IPv4 Addresses\nRFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space\nRFC 5156, Special-Use IPv6 Addresses\n\nWhen the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .\n\nPort (integer) --The port on the endpoint that you want Amazon Route 53 to perform health checks on.\n\nNote\nDon\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .\n\n\nType (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.\n\nWarning\nYou can\'t change the value of Type after you create a health check.\n\nYou can create the following types of health checks:\n\nHTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.\nHTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.\n\n\nWarning\nIf you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.\n\n\nHTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .\nHTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .\nTCP : Route 53 tries to establish a TCP connection.\nCLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .\nCALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .\n\nFor more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .\n\nResourcePath (string) --The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .\n\nFullyQualifiedDomainName (string) --Amazon Route 53 behavior depends on whether you specify a value for IPAddress .\n\nIf you specify a value for IPAddress :\nAmazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.\nWhen Route 53 checks the health of an endpoint, here is how it constructs the Host header:\n\nIf you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.\nIf you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.\nIf you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.\n\nIf you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.\n\n**If you don\'t specify a value for IPAddress ** :\nRoute 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.\n\nNote\nIf you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a 'DNS resolution failed' error.\n\nIf you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).\n\nWarning\nIn this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.\n\nIn addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.\n\nSearchString (string) --If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.\nRoute 53 considers case when searching for SearchString in the response body.\n\nRequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.\n\nWarning\nYou can\'t change the value of RequestInterval after you create a health check.\n\nIf you don\'t specify a value for RequestInterval , the default value is 30 seconds.\n\nFailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .\nIf you don\'t specify a value for FailureThreshold , the default value is three health checks.\n\nMeasureLatency (boolean) --Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.\n\nWarning\nYou can\'t change the value of MeasureLatency after you create a health check.\n\n\nInverted (boolean) --Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.\n\nDisabled (boolean) --Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:\n\nHealth checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.\nCalculated health checks: Route 53 stops aggregating the status of the referenced health checks.\nHealth checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.\n\nAfter you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .\nCharges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .\n\nHealthThreshold (integer) --The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.\nNote the following:\n\nIf you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.\nIf you specify 0 , Route 53 always considers this health check to be healthy.\n\n\nChildHealthChecks (list) --(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.\n\n(string) --\n\n\nEnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.\nSome endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.\nThe SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.\n\nRegions (list) --A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.\nIf you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .\nIf you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).\n\n(string) --\n\n\nAlarmIdentifier (dict) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.\n\nRegion (string) -- [REQUIRED]For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.\nFor the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .\n\nName (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.\n\nNote\nRoute 53 supports CloudWatch alarms with the following features:\n\nStandard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .\nStatistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.\n\n\n\n\n\nInsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:\n\nHealthy : Route 53 considers the health check to be healthy.\nUnhealthy : Route 53 considers the health check to be unhealthy.\nLastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HealthCheck': {
        'Id': 'string',
        'CallerReference': 'string',
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        },
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
            'Disabled': True|False,
            'HealthThreshold': 123,
            'ChildHealthChecks': [
                'string',
            ],
            'EnableSNI': True|False,
            'Regions': [
                'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
            ],
            'AlarmIdentifier': {
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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


Response Structure

(dict) --
A complex type containing the response information for the new health check.

HealthCheck (dict) --
A complex type that contains identifying information about the health check.

Id (string) --
The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

CallerReference (string) --
A unique string that you specified when you created the health check.

LinkedService (dict) --
If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can\'t edit or delete it using Amazon Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.



HealthCheckConfig (dict) --
A complex type that contains detailed information about one health check.

IPAddress (string) --
The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
Use one of the following formats for the value of IPAddress :

IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .

If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
For more information, see FullyQualifiedDomainName .
Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:

RFC 5735, Special Use IPv4 Addresses
RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
RFC 5156, Special-Use IPv6 Addresses

When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .

Port (integer) --
The port on the endpoint that you want Amazon Route 53 to perform health checks on.

Note
Don\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .


Type (string) --
The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

Warning
You can\'t change the value of Type after you create a health check.

You can create the following types of health checks:

HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.


Warning
If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.


HTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
HTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
TCP : Route 53 tries to establish a TCP connection.
CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
CALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .

For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .

ResourcePath (string) --
The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .

FullyQualifiedDomainName (string) --
Amazon Route 53 behavior depends on whether you specify a value for IPAddress .

If you specify a value for IPAddress :

Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
When Route 53 checks the health of an endpoint, here is how it constructs the Host header:

If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.

If you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.

**If you don\'t specify a value for IPAddress ** :

Route 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

Note
If you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a "DNS resolution failed" error.

If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

Warning
In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.

SearchString (string) --
If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
Route 53 considers case when searching for SearchString in the response body.

RequestInterval (integer) --
The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.

Warning
You can\'t change the value of RequestInterval after you create a health check.

If you don\'t specify a value for RequestInterval , the default value is 30 seconds.

FailureThreshold (integer) --
The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
If you don\'t specify a value for FailureThreshold , the default value is three health checks.

MeasureLatency (boolean) --
Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.

Warning
You can\'t change the value of MeasureLatency after you create a health check.


Inverted (boolean) --
Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

Disabled (boolean) --
Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:

Health checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.
Calculated health checks: Route 53 stops aggregating the status of the referenced health checks.
Health checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.

After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .
Charges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .

HealthThreshold (integer) --
The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.
Note the following:

If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
If you specify 0 , Route 53 always considers this health check to be healthy.


ChildHealthChecks (list) --
(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.

(string) --


EnableSNI (boolean) --
Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.

Regions (list) --
A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .
If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

(string) --


AlarmIdentifier (dict) --
A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

Region (string) --
For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
For the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .

Name (string) --
The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

Note
Route 53 supports CloudWatch alarms with the following features:

Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.





InsufficientDataHealthStatus (string) --
When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

Healthy : Route 53 considers the health check to be healthy.
Unhealthy : Route 53 considers the health check to be unhealthy.
LastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.




HealthCheckVersion (integer) --
The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.

CloudWatchAlarmConfiguration (dict) --
A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

EvaluationPeriods (integer) --
For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

Threshold (float) --
For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

ComparisonOperator (string) --
For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

Period (integer) --
For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

MetricName (string) --
The name of the CloudWatch metric that the alarm is associated with.

Namespace (string) --
The namespace of the metric that the alarm is associated with. For more information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

Statistic (string) --
For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

Dimensions (list) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

(dict) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

Name (string) --
For the metric that the CloudWatch alarm is associated with, the name of one dimension.

Value (string) --
For the metric that the CloudWatch alarm is associated with, the value of one dimension.









Location (string) --
The unique URL representing the new health check.







Exceptions

Route53.Client.exceptions.TooManyHealthChecks
Route53.Client.exceptions.HealthCheckAlreadyExists
Route53.Client.exceptions.InvalidInput


    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            },
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
                'Disabled': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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
    A unique string that identifies the request and that allows you to retry a failed CreateHealthCheck request without the risk of creating two identical health checks:
    
    If you send a CreateHealthCheck request with the same CallerReference and settings as a previous request, and if the health check doesn\'t exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the settings for the existing health check.
    If you send a CreateHealthCheck request with the same CallerReference as a deleted health check, regardless of the settings, Route 53 returns a HealthCheckAlreadyExists error.
    If you send a CreateHealthCheck request with the same CallerReference as an existing health check but with different settings, Route 53 returns a HealthCheckAlreadyExists error.
    If you send a CreateHealthCheck request with a unique CallerReference but settings identical to an existing health check, Route 53 creates the health check.
    
    
    HealthCheckConfig (dict) -- [REQUIRED]
    A complex type that contains settings for a new health check.
    
    IPAddress (string) --The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
    Use one of the following formats for the value of IPAddress :
    
    IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
    IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .
    
    If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
    For more information, see FullyQualifiedDomainName .
    Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:
    
    RFC 5735, Special Use IPv4 Addresses
    RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
    RFC 5156, Special-Use IPv6 Addresses
    
    When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .
    
    Port (integer) --The port on the endpoint that you want Amazon Route 53 to perform health checks on.
    
    Note
    Don\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .
    
    
    Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.
    
    Warning
    You can\'t change the value of Type after you create a health check.
    
    You can create the following types of health checks:
    
    HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    
    Warning
    If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
    
    
    HTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    HTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
    TCP : Route 53 tries to establish a TCP connection.
    CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
    CALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .
    
    For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
    
    ResourcePath (string) --The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .
    
    FullyQualifiedDomainName (string) --Amazon Route 53 behavior depends on whether you specify a value for IPAddress .
    
    If you specify a value for IPAddress :
    Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
    When Route 53 checks the health of an endpoint, here is how it constructs the Host header:
    
    If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
    If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
    If you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.
    
    If you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.
    
    **If you don\'t specify a value for IPAddress ** :
    Route 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.
    
    Note
    If you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a "DNS resolution failed" error.
    
    If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).
    
    Warning
    In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
    
    In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.
    
    SearchString (string) --If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
    Route 53 considers case when searching for SearchString in the response body.
    
    RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.
    
    Warning
    You can\'t change the value of RequestInterval after you create a health check.
    
    If you don\'t specify a value for RequestInterval , the default value is 30 seconds.
    
    FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
    If you don\'t specify a value for FailureThreshold , the default value is three health checks.
    
    MeasureLatency (boolean) --Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.
    
    Warning
    You can\'t change the value of MeasureLatency after you create a health check.
    
    
    Inverted (boolean) --Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
    
    Disabled (boolean) --Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:
    
    Health checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.
    Calculated health checks: Route 53 stops aggregating the status of the referenced health checks.
    Health checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.
    
    After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .
    Charges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .
    
    HealthThreshold (integer) --The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.
    Note the following:
    
    If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
    If you specify 0 , Route 53 always considers this health check to be healthy.
    
    
    ChildHealthChecks (list) --(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.
    
    (string) --
    
    
    EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
    Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
    The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.
    
    Regions (list) --A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
    If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .
    If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).
    
    (string) --
    
    
    AlarmIdentifier (dict) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
    
    Region (string) -- [REQUIRED]For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
    For the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .
    
    Name (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
    
    Note
    Route 53 supports CloudWatch alarms with the following features:
    
    Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
    Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.
    
    
    
    
    
    InsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
    
    Healthy : Route 53 considers the health check to be healthy.
    Unhealthy : Route 53 considers the health check to be unhealthy.
    LastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
    
    
    
    
    
    """
    pass

def create_hosted_zone(Name=None, VPC=None, CallerReference=None, HostedZoneConfig=None, DelegationSetId=None):
    """
    Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs).
    For more information about charges for hosted zones, see Amazon Route 53 Pricing .
    Note the following:
    When you submit a CreateHostedZone request, the initial status of the hosted zone is PENDING . For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to INSYNC .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hosted_zone(
        Name='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
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
    :param Name: [REQUIRED]\nThe name of the domain. Specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.\nIf you\'re creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in DelegationSet .\n

    :type VPC: dict
    :param VPC: (Private hosted zones only) A complex type that contains information about the Amazon VPC that you\'re associating with this hosted zone.\nYou can specify only one Amazon VPC when you create a private hosted zone. To associate additional Amazon VPCs with the hosted zone, use AssociateVPCWithHostedZone after you create a hosted zone.\n\nVPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.\n\nVPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.\n\n\n

    :type CallerReference: string
    :param CallerReference: [REQUIRED]\nA unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateHostedZone request. CallerReference can be any unique string, for example, a date/time stamp.\n

    :type HostedZoneConfig: dict
    :param HostedZoneConfig: (Optional) A complex type that contains the following optional values:\n\nFor public and private hosted zones, an optional comment\nFor private hosted zones, an optional PrivateZone element\n\nIf you don\'t specify a comment or the PrivateZone element, omit HostedZoneConfig and the other elements.\n\nComment (string) --Any comments that you want to include about the hosted zone.\n\nPrivateZone (boolean) --A value that indicates whether this is a private hosted zone.\n\n\n

    :type DelegationSetId: string
    :param DelegationSetId: If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see CreateReusableDelegationSet .

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZone': {
        'Id': 'string',
        'Name': 'string',
        'CallerReference': 'string',
        'Config': {
            'Comment': 'string',
            'PrivateZone': True|False
        },
        'ResourceRecordSetCount': 123,
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        }
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
        'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
        'VPCId': 'string'
    },
    'Location': 'string'
}


Response Structure

(dict) --
A complex type containing the response information for the hosted zone.

HostedZone (dict) --
A complex type that contains general information about the hosted zone.

Id (string) --
The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name (string) --
The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .

CallerReference (string) --
The value that you specified for CallerReference when you created the hosted zone.

Config (dict) --
A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don\'t appear in the response.

Comment (string) --
Any comments that you want to include about the hosted zone.

PrivateZone (boolean) --
A value that indicates whether this is a private hosted zone.



ResourceRecordSetCount (integer) --
The number of resource record sets in the hosted zone.

LinkedService (dict) --
If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.





ChangeInfo (dict) --
A complex type that contains information about the CreateHostedZone request.

Id (string) --
The ID of the request.

Status (string) --
The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt (datetime) --
The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --
A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.



DelegationSet (dict) --
A complex type that describes the name servers for this hosted zone.

Id (string) --
The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference (string) --
The value that you specified for CallerReference when you created the reusable delegation set.

NameServers (list) --
A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string) --




VPC (dict) --
A complex type that contains information about an Amazon VPC that you associated with this hosted zone.

VPCRegion (string) --
(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId (string) --
(Private hosted zones only) The ID of an Amazon VPC.



Location (string) --
The unique URL representing the new hosted zone.







Exceptions

Route53.Client.exceptions.InvalidDomainName
Route53.Client.exceptions.HostedZoneAlreadyExists
Route53.Client.exceptions.TooManyHostedZones
Route53.Client.exceptions.InvalidVPCId
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.DelegationSetNotAvailable
Route53.Client.exceptions.ConflictingDomainExists
Route53.Client.exceptions.NoSuchDelegationSet
Route53.Client.exceptions.DelegationSetNotReusable


    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
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
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    The name of the domain. Specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
    If you\'re creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in DelegationSet .
    
    VPC (dict) -- (Private hosted zones only) A complex type that contains information about the Amazon VPC that you\'re associating with this hosted zone.
    You can specify only one Amazon VPC when you create a private hosted zone. To associate additional Amazon VPCs with the hosted zone, use AssociateVPCWithHostedZone after you create a hosted zone.
    
    VPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.
    
    VPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.
    
    
    
    CallerReference (string) -- [REQUIRED]
    A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateHostedZone request. CallerReference can be any unique string, for example, a date/time stamp.
    
    HostedZoneConfig (dict) -- (Optional) A complex type that contains the following optional values:
    
    For public and private hosted zones, an optional comment
    For private hosted zones, an optional PrivateZone element
    
    If you don\'t specify a comment or the PrivateZone element, omit HostedZoneConfig and the other elements.
    
    Comment (string) --Any comments that you want to include about the hosted zone.
    
    PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.
    
    
    
    DelegationSetId (string) -- If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see CreateReusableDelegationSet .
    
    """
    pass

def create_query_logging_config(HostedZoneId=None, CloudWatchLogsLogGroupArn=None):
    """
    Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.
    DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:
    Before you create a query logging configuration, perform the following operations.
    When Route 53 finishes creating the configuration for DNS query logging, it does the following:
    The name of each log stream is in the following format:
    The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the Route 53 Product Details page.
    Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn\'t forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see Routing Internet Traffic to Your Website or Web Application in the Amazon Route 53 Developer Guide .
    For a list of the values in each query log and the format of each value, see Logging DNS Queries in the Amazon Route 53 Developer Guide .
    For information about charges for query logs, see Amazon CloudWatch Pricing .
    If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see DeleteQueryLoggingConfig .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_query_logging_config(
        HostedZoneId='string',
        CloudWatchLogsLogGroupArn='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.\n

    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:\narn:aws:logs:region :account-id :log-group:log_group_name\nTo get the ARN for a log group, you can use the CloudWatch console, the DescribeLogGroups API action, the describe-log-groups command, or the applicable command in one of the AWS SDKs.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'QueryLoggingConfig': {
        'Id': 'string',
        'HostedZoneId': 'string',
        'CloudWatchLogsLogGroupArn': 'string'
    },
    'Location': 'string'
}


Response Structure

(dict) --

QueryLoggingConfig (dict) --
A complex type that contains the ID for a query logging configuration, the ID of the hosted zone that you want to log queries for, and the ARN for the log group that you want Amazon Route 53 to send query logs to.

Id (string) --
The ID for a configuration for DNS query logging.

HostedZoneId (string) --
The ID of the hosted zone that CloudWatch Logs is logging queries for.

CloudWatchLogsLogGroupArn (string) --
The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.



Location (string) --
The unique URL representing the new query logging configuration.







Exceptions

Route53.Client.exceptions.ConcurrentModification
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.NoSuchCloudWatchLogsLogGroup
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.QueryLoggingConfigAlreadyExists
Route53.Client.exceptions.InsufficientCloudWatchLogsResourcePolicy


    :return: {
        'QueryLoggingConfig': {
            'Id': 'string',
            'HostedZoneId': 'string',
            'CloudWatchLogsLogGroupArn': 'string'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.
    Begins to send query logs to the applicable log stream.
    
    """
    pass

def create_reusable_delegation_set(CallerReference=None, HostedZoneId=None):
    """
    Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same AWS account.
    You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the CreateReusableDelegationSet request.
    For information about using a reusable delegation set to configure white label name servers, see Configuring White Label Name Servers .
    The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:
    If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones can\'t use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_reusable_delegation_set(
        CallerReference='string',
        HostedZoneId='string'
    )
    
    
    :type CallerReference: string
    :param CallerReference: [REQUIRED]\nA unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example a date/time stamp.\n

    :type HostedZoneId: string
    :param HostedZoneId: If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.

    :rtype: dict

ReturnsResponse Syntax
{
    'DelegationSet': {
        'Id': 'string',
        'CallerReference': 'string',
        'NameServers': [
            'string',
        ]
    },
    'Location': 'string'
}


Response Structure

(dict) --

DelegationSet (dict) --
A complex type that contains name server information.

Id (string) --
The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference (string) --
The value that you specified for CallerReference when you created the reusable delegation set.

NameServers (list) --
A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string) --




Location (string) --
The unique URL representing the new reusable delegation set.







Exceptions

Route53.Client.exceptions.DelegationSetAlreadyCreated
Route53.Client.exceptions.LimitsExceeded
Route53.Client.exceptions.HostedZoneNotFound
Route53.Client.exceptions.InvalidArgument
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.DelegationSetNotAvailable
Route53.Client.exceptions.DelegationSetAlreadyReusable


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
    For small numbers of hosted zones\xe2\x80\x94up to a few hundred\xe2\x80\x94it\'s relatively easy to create reusable delegation sets until you get one that has four name servers that don\'t overlap with any of the name servers in your hosted zones.
    For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.
    For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don\'t have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.
    
    """
    pass

def create_traffic_policy(Name=None, Document=None, Comment=None):
    """
    Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_traffic_policy(
        Name='string',
        Document='string',
        Comment='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the traffic policy.\n

    :type Document: string
    :param Document: [REQUIRED]\nThe definition of this traffic policy in JSON format. For more information, see Traffic Policy Document Format .\n

    :type Comment: string
    :param Comment: (Optional) Any comments that you want to include about the traffic policy.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicy': {
        'Id': 'string',
        'Version': 123,
        'Name': 'string',
        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'Document': 'string',
        'Comment': 'string'
    },
    'Location': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the CreateTrafficPolicy request.

TrafficPolicy (dict) --
A complex type that contains settings for the new traffic policy.

Id (string) --
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

Version (integer) --
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of Version is always 1.

Name (string) --
The name that you specified when you created the traffic policy.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

Document (string) --
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the CreateTrafficPolicy request. For more information about the JSON format, see Traffic Policy Document Format .

Comment (string) --
The comment that you specify in the CreateTrafficPolicy request, if any.



Location (string) --
A unique URL that represents a new traffic policy.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.TooManyTrafficPolicies
Route53.Client.exceptions.TrafficPolicyAlreadyExists
Route53.Client.exceptions.InvalidTrafficPolicyDocument


    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'Document': 'string',
            'Comment': 'string'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.TooManyTrafficPolicies
    Route53.Client.exceptions.TrafficPolicyAlreadyExists
    Route53.Client.exceptions.InvalidTrafficPolicyDocument
    
    """
    pass

def create_traffic_policy_instance(HostedZoneId=None, Name=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
    """
    Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, CreateTrafficPolicyInstance associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that CreateTrafficPolicyInstance created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_traffic_policy_instance(
        HostedZoneId='string',
        Name='string',
        TTL=123,
        TrafficPolicyId='string',
        TrafficPolicyVersion=123
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that you want Amazon Route 53 to create resource record sets in by using the configuration in a traffic policy.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Route 53 creates for this traffic policy instance.\n

    :type TTL: integer
    :param TTL: [REQUIRED]\n(Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.\n

    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]\nThe ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.\n

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]\nThe version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicyInstance': {
        'Id': 'string',
        'HostedZoneId': 'string',
        'Name': 'string',
        'TTL': 123,
        'State': 'string',
        'Message': 'string',
        'TrafficPolicyId': 'string',
        'TrafficPolicyVersion': 123,
        'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
    },
    'Location': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the CreateTrafficPolicyInstance request.

TrafficPolicyInstance (dict) --
A complex type that contains settings for the new traffic policy instance.

Id (string) --
The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId (string) --
The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name (string) --
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL (integer) --
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State (string) --
The value of State is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed

Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --
If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.



Location (string) --
A unique URL that represents a new traffic policy instance.







Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.TooManyTrafficPolicyInstances
Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.TrafficPolicyInstanceAlreadyExists


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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.TooManyTrafficPolicyInstances
    Route53.Client.exceptions.NoSuchTrafficPolicy
    Route53.Client.exceptions.TrafficPolicyInstanceAlreadyExists
    
    """
    pass

def create_traffic_policy_version(Id=None, Document=None, Comment=None):
    """
    Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you\'ll need to start a new traffic policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_traffic_policy_version(
        Id='string',
        Document='string',
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy for which you want to create a new version.\n

    :type Document: string
    :param Document: [REQUIRED]\nThe definition of this version of the traffic policy, in JSON format. You specified the JSON in the CreateTrafficPolicyVersion request. For more information about the JSON format, see CreateTrafficPolicy .\n

    :type Comment: string
    :param Comment: The comment that you specified in the CreateTrafficPolicyVersion request, if any.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicy': {
        'Id': 'string',
        'Version': 123,
        'Name': 'string',
        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'Document': 'string',
        'Comment': 'string'
    },
    'Location': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the CreateTrafficPolicyVersion request.

TrafficPolicy (dict) --
A complex type that contains settings for the new version of the traffic policy.

Id (string) --
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

Version (integer) --
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of Version is always 1.

Name (string) --
The name that you specified when you created the traffic policy.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

Document (string) --
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the CreateTrafficPolicy request. For more information about the JSON format, see Traffic Policy Document Format .

Comment (string) --
The comment that you specify in the CreateTrafficPolicy request, if any.



Location (string) --
A unique URL that represents a new traffic policy version.







Exceptions

Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.TooManyTrafficPolicyVersionsForCurrentPolicy
Route53.Client.exceptions.ConcurrentModification
Route53.Client.exceptions.InvalidTrafficPolicyDocument


    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'Document': 'string',
            'Comment': 'string'
        },
        'Location': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchTrafficPolicy
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.TooManyTrafficPolicyVersionsForCurrentPolicy
    Route53.Client.exceptions.ConcurrentModification
    Route53.Client.exceptions.InvalidTrafficPolicyDocument
    
    """
    pass

def create_vpc_association_authorization(HostedZoneId=None, VPC=None):
    """
    Authorizes the AWS account that created a specified VPC to submit an AssociateVPCWithHostedZone request to associate the VPC with a specified hosted zone that was created by a different account. To submit a CreateVPCAssociationAuthorization request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an AssociateVPCWithHostedZone request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vpc_association_authorization(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        }
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the private hosted zone that you want to authorize associating a VPC with.\n

    :type VPC: dict
    :param VPC: [REQUIRED]\nA complex type that contains the VPC ID and region for the VPC that you want to authorize associating with your hosted zone.\n\nVPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.\n\nVPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZoneId': 'string',
    'VPC': {
        'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
        'VPCId': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information from a CreateVPCAssociationAuthorization request.

HostedZoneId (string) --
The ID of the hosted zone that you authorized associating a VPC with.

VPC (dict) --
The VPC that you authorized associating with a hosted zone.

VPCRegion (string) --
(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId (string) --
(Private hosted zones only) The ID of an Amazon VPC.









Exceptions

Route53.Client.exceptions.ConcurrentModification
Route53.Client.exceptions.TooManyVPCAssociationAuthorizations
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidVPCId
Route53.Client.exceptions.InvalidInput


    :return: {
        'HostedZoneId': 'string',
        'VPC': {
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.ConcurrentModification
    Route53.Client.exceptions.TooManyVPCAssociationAuthorizations
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidVPCId
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def delete_health_check(HealthCheckId=None):
    """
    Deletes a health check.
    If you\'re using AWS Cloud Map and you configured Cloud Map to create a Route 53 health check when you register an instance, you can\'t use the Route 53 DeleteHealthCheck command to delete the health check. The health check is deleted automatically when you deregister the instance; there can be a delay of several hours before the health check is deleted from Route 53.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_health_check(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]\nThe ID of the health check that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --An empty element.




Exceptions

Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.HealthCheckInUse
Route53.Client.exceptions.InvalidInput


    :return: {}
    
    
    """
    pass

def delete_hosted_zone(Id=None):
    """
    Deletes a hosted zone.
    If the hosted zone was created by another service, such as AWS Cloud Map, see Deleting Public Hosted Zones That Were Created by Another Service in the Amazon Route 53 Developer Guide for information about how to delete it. (The process is the same for public and private hosted zones that were created by another service.)
    If you want to keep your domain registration but you want to stop routing internet traffic to your website or web application, we recommend that you delete resource record sets in the hosted zone instead of deleting the hosted zone.
    If you want to avoid the monthly charge for the hosted zone, you can transfer DNS service for the domain to a free DNS service. When you transfer DNS service, you have to update the name servers for the domain registration. If the domain is registered with Route 53, see UpdateDomainNameservers for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by the registrar to update name servers for the domain registration. For more information, perform an internet search on "free DNS service."
    You can delete a hosted zone only if it contains only the default SOA record and NS resource record sets. If the hosted zone contains other resource record sets, you must delete them before you can delete the hosted zone. If you try to delete a hosted zone that contains other resource record sets, the request fails, and Route 53 returns a HostedZoneNotEmpty error. For information about deleting records from your hosted zone, see ChangeResourceRecordSets .
    To verify that the hosted zone has been deleted, do one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hosted_zone(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the hosted zone you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ChangeInfo': {
        'Id': 'string',
        'Status': 'PENDING'|'INSYNC',
        'SubmittedAt': datetime(2015, 1, 1),
        'Comment': 'string'
    }
}


Response Structure

(dict) --A complex type that contains the response to a DeleteHostedZone request.

ChangeInfo (dict) --A complex type that contains the ID, the status, and the date and time of a request to delete a hosted zone.

Id (string) --The ID of the request.

Status (string) --The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt (datetime) --The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.








Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.HostedZoneNotEmpty
Route53.Client.exceptions.PriorRequestNotComplete
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.InvalidDomainName


    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.HostedZoneNotEmpty
    Route53.Client.exceptions.PriorRequestNotComplete
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.InvalidDomainName
    
    """
    pass

def delete_query_logging_config(Id=None):
    """
    Deletes a configuration for DNS query logging. If you delete a configuration, Amazon Route 53 stops sending query logs to CloudWatch Logs. Route 53 doesn\'t delete any logs that are already in CloudWatch Logs.
    For more information about DNS query logs, see CreateQueryLoggingConfig .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_query_logging_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the configuration that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Route53.Client.exceptions.ConcurrentModification
Route53.Client.exceptions.NoSuchQueryLoggingConfig
Route53.Client.exceptions.InvalidInput


    :return: {}
    
    
    :returns: 
    Route53.Client.exceptions.ConcurrentModification
    Route53.Client.exceptions.NoSuchQueryLoggingConfig
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def delete_reusable_delegation_set(Id=None):
    """
    Deletes a reusable delegation set.
    To verify that the reusable delegation set is not associated with any hosted zones, submit a GetReusableDelegationSet request and specify the ID of the reusable delegation set that you want to delete.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_reusable_delegation_set(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the reusable delegation set that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --An empty element.




Exceptions

Route53.Client.exceptions.NoSuchDelegationSet
Route53.Client.exceptions.DelegationSetInUse
Route53.Client.exceptions.DelegationSetNotReusable
Route53.Client.exceptions.InvalidInput


    :return: {}
    
    
    """
    pass

def delete_traffic_policy(Id=None, Version=None):
    """
    Deletes a traffic policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_traffic_policy(
        Id='string',
        Version=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy that you want to delete.\n

    :type Version: integer
    :param Version: [REQUIRED]\nThe version number of the traffic policy that you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
An empty element.





Exceptions

Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.TrafficPolicyInUse
Route53.Client.exceptions.ConcurrentModification


    :return: {}
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchTrafficPolicy
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.TrafficPolicyInUse
    Route53.Client.exceptions.ConcurrentModification
    
    """
    pass

def delete_traffic_policy_instance(Id=None):
    """
    Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_traffic_policy_instance(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy instance that you want to delete.\n\nWarning\nWhen you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --An empty element.




Exceptions

Route53.Client.exceptions.NoSuchTrafficPolicyInstance
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.PriorRequestNotComplete


    :return: {}
    
    
    """
    pass

def delete_vpc_association_authorization(HostedZoneId=None, VPC=None):
    """
    Removes authorization to submit an AssociateVPCWithHostedZone request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a DeleteVPCAssociationAuthorization request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vpc_association_authorization(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        }
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nWhen removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, the ID of the hosted zone.\n

    :type VPC: dict
    :param VPC: [REQUIRED]\nWhen removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, a complex type that includes the ID and region of the VPC.\n\nVPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.\n\nVPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Empty response for the request.





Exceptions

Route53.Client.exceptions.ConcurrentModification
Route53.Client.exceptions.VPCAssociationAuthorizationNotFound
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidVPCId
Route53.Client.exceptions.InvalidInput


    :return: {}
    
    
    :returns: 
    Route53.Client.exceptions.ConcurrentModification
    Route53.Client.exceptions.VPCAssociationAuthorizationNotFound
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidVPCId
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def disassociate_vpc_from_hosted_zone(HostedZoneId=None, VPC=None, Comment=None):
    """
    Disassociates a VPC from a Amazon Route 53 private hosted zone. Note the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_vpc_from_hosted_zone(
        HostedZoneId='string',
        VPC={
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        },
        Comment='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the private hosted zone that you want to disassociate a VPC from.\n

    :type VPC: dict
    :param VPC: [REQUIRED]\nA complex type that contains information about the VPC that you\'re disassociating from the specified hosted zone.\n\nVPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.\n\nVPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.\n\n\n

    :type Comment: string
    :param Comment: Optional: A comment about the disassociation request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeInfo': {
        'Id': 'string',
        'Status': 'PENDING'|'INSYNC',
        'SubmittedAt': datetime(2015, 1, 1),
        'Comment': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information for the disassociate request.

ChangeInfo (dict) --
A complex type that describes the changes made to the specified private hosted zone.

Id (string) --
The ID of the request.

Status (string) --
The current state of the request. PENDING indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt (datetime) --
The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --
A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.









Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidVPCId
Route53.Client.exceptions.VPCAssociationNotFound
Route53.Client.exceptions.LastVPCAssociation
Route53.Client.exceptions.InvalidInput


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
    The ID of the private hosted zone that you want to disassociate a VPC from.
    
    VPC (dict) -- [REQUIRED]
    A complex type that contains information about the VPC that you\'re disassociating from the specified hosted zone.
    
    VPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.
    
    VPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.
    
    
    
    Comment (string) -- Optional: A comment about the disassociation request.
    
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

def get_account_limit(Type=None):
    """
    Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.
    For the default limit, see Limits in the Amazon Route 53 Developer Guide . To request a higher limit, open a case .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_account_limit(
        Type='MAX_HEALTH_CHECKS_BY_OWNER'|'MAX_HOSTED_ZONES_BY_OWNER'|'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER'|'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER'|'MAX_TRAFFIC_POLICIES_BY_OWNER'
    )
    
    
    :type Type: string
    :param Type: [REQUIRED]\nThe limit that you want to get. Valid values include the following:\n\nMAX_HEALTH_CHECKS_BY_OWNER : The maximum number of health checks that you can create using the current account.\nMAX_HOSTED_ZONES_BY_OWNER : The maximum number of hosted zones that you can create using the current account.\nMAX_REUSABLE_DELEGATION_SETS_BY_OWNER : The maximum number of reusable delegation sets that you can create using the current account.\nMAX_TRAFFIC_POLICIES_BY_OWNER : The maximum number of traffic policies that you can create using the current account.\nMAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Limit': {
        'Type': 'MAX_HEALTH_CHECKS_BY_OWNER'|'MAX_HOSTED_ZONES_BY_OWNER'|'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER'|'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER'|'MAX_TRAFFIC_POLICIES_BY_OWNER',
        'Value': 123
    },
    'Count': 123
}


Response Structure

(dict) --A complex type that contains the requested limit.

Limit (dict) --The current setting for the specified limit. For example, if you specified MAX_HEALTH_CHECKS_BY_OWNER for the value of Type in the request, the value of Limit is the maximum number of health checks that you can create using the current account.

Type (string) --The limit that you requested. Valid values include the following:

MAX_HEALTH_CHECKS_BY_OWNER : The maximum number of health checks that you can create using the current account.
MAX_HOSTED_ZONES_BY_OWNER : The maximum number of hosted zones that you can create using the current account.
MAX_REUSABLE_DELEGATION_SETS_BY_OWNER : The maximum number of reusable delegation sets that you can create using the current account.
MAX_TRAFFIC_POLICIES_BY_OWNER : The maximum number of traffic policies that you can create using the current account.
MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)


Value (integer) --The current value for the limit that is specified by Type .



Count (integer) --The current number of entities that you have created of the specified type. For example, if you specified MAX_HEALTH_CHECKS_BY_OWNER for the value of Type in the request, the value of Count is the current number of health checks that you have created using the current account.






Exceptions

Route53.Client.exceptions.InvalidInput


    :return: {
        'Limit': {
            'Type': 'MAX_HEALTH_CHECKS_BY_OWNER'|'MAX_HOSTED_ZONES_BY_OWNER'|'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER'|'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER'|'MAX_TRAFFIC_POLICIES_BY_OWNER',
            'Value': 123
        },
        'Count': 123
    }
    
    
    :returns: 
    MAX_HEALTH_CHECKS_BY_OWNER : The maximum number of health checks that you can create using the current account.
    MAX_HOSTED_ZONES_BY_OWNER : The maximum number of hosted zones that you can create using the current account.
    MAX_REUSABLE_DELEGATION_SETS_BY_OWNER : The maximum number of reusable delegation sets that you can create using the current account.
    MAX_TRAFFIC_POLICIES_BY_OWNER : The maximum number of traffic policies that you can create using the current account.
    MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER : The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)
    
    """
    pass

def get_change(Id=None):
    """
    Returns the current status of a change batch request. The status is one of the following values:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_change(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the change batch request. The value that you specify here is the value that ChangeResourceRecordSets returned in the Id element when you submitted the request.\n

    :rtype: dict
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

SubmittedAt (datetime) --The date and time that the change request was submitted in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.

Comment (string) --A complex type that describes change information about changes made to your hosted zone.
This element contains an ID that you use when performing a GetChange action to get detailed information about the change.








Exceptions

Route53.Client.exceptions.NoSuchChange
Route53.Client.exceptions.InvalidInput


    :return: {
        'ChangeInfo': {
            'Id': 'string',
            'Status': 'PENDING'|'INSYNC',
            'SubmittedAt': datetime(2015, 1, 1),
            'Comment': 'string'
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchChange
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def get_checker_ip_ranges():
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_checker_ip_ranges()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'CheckerIpRanges': [
        'string',
    ]
}


Response Structure

(dict) --A complex type that contains the CheckerIpRanges element.

CheckerIpRanges (list) --A complex type that contains sorted list of IP ranges in CIDR format for Amazon Route 53 health checkers.

(string) --








    :return: {
        'CheckerIpRanges': [
            'string',
        ]
    }
    
    
    """
    pass

def get_geo_location(ContinentCode=None, CountryCode=None, SubdivisionCode=None):
    """
    Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.
    Use the following syntax to determine whether a continent is supported for geolocation:
    Use the following syntax to determine whether a country is supported for geolocation:
    Use the following syntax to determine whether a subdivision of a country is supported for geolocation:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_geo_location(
        ContinentCode='string',
        CountryCode='string',
        SubdivisionCode='string'
    )
    
    
    :type ContinentCode: string
    :param ContinentCode: For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:\n\nAF : Africa\nAN : Antarctica\nAS : Asia\nEU : Europe\nOC : Oceania\nNA : North America\nSA : South America\n\n

    :type CountryCode: string
    :param CountryCode: Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .

    :type SubdivisionCode: string
    :param SubdivisionCode: For SubdivisionCode , Amazon Route 53 supports only states of the United States. For a list of state abbreviations, see Appendix B: Two\xe2\x80\x93Letter State and Possession Abbreviations on the United States Postal Service website.\nIf you specify subdivisioncode , you must also specify US for CountryCode .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GeoLocationDetails': {
        'ContinentCode': 'string',
        'ContinentName': 'string',
        'CountryCode': 'string',
        'CountryName': 'string',
        'SubdivisionCode': 'string',
        'SubdivisionName': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information for the specified geolocation code.

GeoLocationDetails (dict) --
A complex type that contains the codes and full continent, country, and subdivision names for the specified geolocation code.

ContinentCode (string) --
The two-letter code for the continent.

ContinentName (string) --
The full name of the continent.

CountryCode (string) --
The two-letter code for the country.

CountryName (string) --
The name of the country.

SubdivisionCode (string) --
The code for the subdivision. Route 53 currently supports only states in the United States.

SubdivisionName (string) --
The full name of the subdivision. Route 53 currently supports only states in the United States.









Exceptions

Route53.Client.exceptions.NoSuchGeoLocation
Route53.Client.exceptions.InvalidInput


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
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchGeoLocation
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def get_health_check(HealthCheckId=None):
    """
    Gets information about a specified health check.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_health_check(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]\nThe identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HealthCheck': {
        'Id': 'string',
        'CallerReference': 'string',
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        },
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
            'Disabled': True|False,
            'HealthThreshold': 123,
            'ChildHealthChecks': [
                'string',
            ],
            'EnableSNI': True|False,
            'Regions': [
                'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
            ],
            'AlarmIdentifier': {
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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

LinkedService (dict) --If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can\'t edit or delete it using Amazon Route 53.

ServicePrincipal (string) --If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.



HealthCheckConfig (dict) --A complex type that contains detailed information about one health check.

IPAddress (string) --The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
Use one of the following formats for the value of IPAddress :

IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .

If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
For more information, see FullyQualifiedDomainName .
Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:

RFC 5735, Special Use IPv4 Addresses
RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
RFC 5156, Special-Use IPv6 Addresses

When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .

Port (integer) --The port on the endpoint that you want Amazon Route 53 to perform health checks on.

Note
Don\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .


Type (string) --The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

Warning
You can\'t change the value of Type after you create a health check.

You can create the following types of health checks:

HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.


Warning
If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.


HTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
HTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
TCP : Route 53 tries to establish a TCP connection.
CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
CALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .

For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .

ResourcePath (string) --The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .

FullyQualifiedDomainName (string) --Amazon Route 53 behavior depends on whether you specify a value for IPAddress .

If you specify a value for IPAddress :
Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
When Route 53 checks the health of an endpoint, here is how it constructs the Host header:

If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.

If you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.

**If you don\'t specify a value for IPAddress ** :
Route 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

Note
If you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a "DNS resolution failed" error.

If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

Warning
In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.

SearchString (string) --If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
Route 53 considers case when searching for SearchString in the response body.

RequestInterval (integer) --The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.

Warning
You can\'t change the value of RequestInterval after you create a health check.

If you don\'t specify a value for RequestInterval , the default value is 30 seconds.

FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
If you don\'t specify a value for FailureThreshold , the default value is three health checks.

MeasureLatency (boolean) --Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.

Warning
You can\'t change the value of MeasureLatency after you create a health check.


Inverted (boolean) --Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

Disabled (boolean) --Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:

Health checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.
Calculated health checks: Route 53 stops aggregating the status of the referenced health checks.
Health checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.

After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .
Charges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .

HealthThreshold (integer) --The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.
Note the following:

If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
If you specify 0 , Route 53 always considers this health check to be healthy.


ChildHealthChecks (list) --(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.

(string) --


EnableSNI (boolean) --Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.

Regions (list) --A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .
If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

(string) --


AlarmIdentifier (dict) --A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

Region (string) --For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
For the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .

Name (string) --The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

Note
Route 53 supports CloudWatch alarms with the following features:

Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.





InsufficientDataHealthStatus (string) --When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

Healthy : Route 53 considers the health check to be healthy.
Unhealthy : Route 53 considers the health check to be unhealthy.
LastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.




HealthCheckVersion (integer) --The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.

CloudWatchAlarmConfiguration (dict) --A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

EvaluationPeriods (integer) --For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

Threshold (float) --For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

ComparisonOperator (string) --For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

Period (integer) --For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

MetricName (string) --The name of the CloudWatch metric that the alarm is associated with.

Namespace (string) --The namespace of the metric that the alarm is associated with. For more information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

Statistic (string) --For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

Dimensions (list) --For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

(dict) --For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

Name (string) --For the metric that the CloudWatch alarm is associated with, the name of one dimension.

Value (string) --For the metric that the CloudWatch alarm is associated with, the value of one dimension.














Exceptions

Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.IncompatibleVersion


    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            },
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
                'Disabled': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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
    RFC 5735, Special Use IPv4 Addresses
    RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
    RFC 5156, Special-Use IPv6 Addresses
    
    """
    pass

def get_health_check_count():
    """
    Retrieves the number of health checks that are associated with the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_health_check_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'HealthCheckCount': 123
}


Response Structure

(dict) --A complex type that contains the response to a GetHealthCheckCount request.

HealthCheckCount (integer) --The number of health checks associated with the current AWS account.







    :return: {
        'HealthCheckCount': 123
    }
    
    
    """
    pass

def get_health_check_last_failure_reason(HealthCheckId=None):
    """
    Gets the reason that a specified health check failed most recently.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_health_check_last_failure_reason(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]\nThe ID for the health check for which you want the last failure reason. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.\n\nNote\nIf you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can\'t use GetHealthCheckLastFailureReason for a calculated health check.\n\n

    :rtype: dict
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

Region (string) --The region of the Amazon Route 53 health checker that provided the status in StatusReport .

IPAddress (string) --The IP address of the Amazon Route 53 health checker that provided the failure reason in StatusReport .

StatusReport (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.

Status (string) --A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.

CheckedTime (datetime) --The date and time that the health checker performed the health check in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.












Exceptions

Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.InvalidInput


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
    Gets status of a specified health check.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_health_check_status(
        HealthCheckId='string'
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]\nThe ID for the health check that you want the current status for. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.\n\nNote\nIf you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can\'t use GetHealthCheckStatus to get the status of a calculated health check.\n\n

    :rtype: dict
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

Region (string) --The region of the Amazon Route 53 health checker that provided the status in StatusReport .

IPAddress (string) --The IP address of the Amazon Route 53 health checker that provided the failure reason in StatusReport .

StatusReport (dict) --A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.

Status (string) --A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.

CheckedTime (datetime) --The date and time that the health checker performed the health check in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2017-03-27T17:48:16.751Z represents March 27, 2017 at 17:48:16.751 UTC.












Exceptions

Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.InvalidInput


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
    Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about the Z3M3LMPEXAMPLE hosted zone.
    Expected Output:
    
    :example: response = client.get_hosted_zone(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the hosted zone that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HostedZone': {
        'Id': 'string',
        'Name': 'string',
        'CallerReference': 'string',
        'Config': {
            'Comment': 'string',
            'PrivateZone': True|False
        },
        'ResourceRecordSetCount': 123,
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        }
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
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        },
    ]
}


Response Structure

(dict) --A complex type that contain the response to a GetHostedZone request.

HostedZone (dict) --A complex type that contains general information about the specified hosted zone.

Id (string) --The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name (string) --The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .

CallerReference (string) --The value that you specified for CallerReference when you created the hosted zone.

Config (dict) --A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don\'t appear in the response.

Comment (string) --Any comments that you want to include about the hosted zone.

PrivateZone (boolean) --A value that indicates whether this is a private hosted zone.



ResourceRecordSetCount (integer) --The number of resource record sets in the hosted zone.

LinkedService (dict) --If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53.

ServicePrincipal (string) --If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.





DelegationSet (dict) --A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.

Id (string) --The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference (string) --The value that you specified for CallerReference when you created the reusable delegation set.

NameServers (list) --A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string) --




VPCs (list) --A complex type that contains information about the VPCs that are associated with the specified hosted zone.

(dict) --(Private hosted zones only) A complex type that contains information about an Amazon VPC.

VPCRegion (string) --(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId (string) --(Private hosted zones only) The ID of an Amazon VPC.










Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput

Examples
The following example gets information about the Z3M3LMPEXAMPLE hosted zone.
response = client.get_hosted_zone(
    Id='Z3M3LMPEXAMPLE',
)

print(response)


Expected Output:
{
    'DelegationSet': {
        'NameServers': [
            'ns-2048.awsdns-64.com',
            'ns-2049.awsdns-65.net',
            'ns-2050.awsdns-66.org',
            'ns-2051.awsdns-67.co.uk',
        ],
    },
    'HostedZone': {
        'CallerReference': 'C741617D-04E4-F8DE-B9D7-0D150FC61C2E',
        'Config': {
            'PrivateZone': False,
        },
        'Id': '/hostedzone/Z3M3LMPEXAMPLE',
        'Name': 'myawsbucket.com.',
        'ResourceRecordSetCount': 8,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
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
                'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
                'VPCId': 'string'
            },
        ]
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def get_hosted_zone_count():
    """
    Retrieves the number of hosted zones that are associated with the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_hosted_zone_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'HostedZoneCount': 123
}


Response Structure

(dict) --A complex type that contains the response to a GetHostedZoneCount request.

HostedZoneCount (integer) --The total number of public and private hosted zones that are associated with the current AWS account.






Exceptions

Route53.Client.exceptions.InvalidInput


    :return: {
        'HostedZoneCount': 123
    }
    
    
    """
    pass

def get_hosted_zone_limit(Type=None, HostedZoneId=None):
    """
    Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone.
    For the default limit, see Limits in the Amazon Route 53 Developer Guide . To request a higher limit, open a case .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_hosted_zone_limit(
        Type='MAX_RRSETS_BY_ZONE'|'MAX_VPCS_ASSOCIATED_BY_ZONE',
        HostedZoneId='string'
    )
    
    
    :type Type: string
    :param Type: [REQUIRED]\nThe limit that you want to get. Valid values include the following:\n\nMAX_RRSETS_BY_ZONE : The maximum number of records that you can create in the specified hosted zone.\nMAX_VPCS_ASSOCIATED_BY_ZONE : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.\n\n

    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that you want to get a limit for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Limit': {
        'Type': 'MAX_RRSETS_BY_ZONE'|'MAX_VPCS_ASSOCIATED_BY_ZONE',
        'Value': 123
    },
    'Count': 123
}


Response Structure

(dict) --
A complex type that contains the requested limit.

Limit (dict) --
The current setting for the specified limit. For example, if you specified MAX_RRSETS_BY_ZONE for the value of Type in the request, the value of Limit is the maximum number of records that you can create in the specified hosted zone.

Type (string) --
The limit that you requested. Valid values include the following:

MAX_RRSETS_BY_ZONE : The maximum number of records that you can create in the specified hosted zone.
MAX_VPCS_ASSOCIATED_BY_ZONE : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.


Value (integer) --
The current value for the limit that is specified by Type .



Count (integer) --
The current number of entities that you have created of the specified type. For example, if you specified MAX_RRSETS_BY_ZONE for the value of Type in the request, the value of Count is the current number of records that you have created in the specified hosted zone.







Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.HostedZoneNotPrivate


    :return: {
        'Limit': {
            'Type': 'MAX_RRSETS_BY_ZONE'|'MAX_VPCS_ASSOCIATED_BY_ZONE',
            'Value': 123
        },
        'Count': 123
    }
    
    
    :returns: 
    MAX_RRSETS_BY_ZONE : The maximum number of records that you can create in the specified hosted zone.
    MAX_VPCS_ASSOCIATED_BY_ZONE : The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.
    
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

def get_query_logging_config(Id=None):
    """
    Gets information about a specified configuration for DNS query logging.
    For more information about DNS query logs, see CreateQueryLoggingConfig and Logging DNS Queries .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_query_logging_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the configuration for DNS query logging that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'QueryLoggingConfig': {
        'Id': 'string',
        'HostedZoneId': 'string',
        'CloudWatchLogsLogGroupArn': 'string'
    }
}


Response Structure

(dict) --
QueryLoggingConfig (dict) --A complex type that contains information about the query logging configuration that you specified in a GetQueryLoggingConfig request.

Id (string) --The ID for a configuration for DNS query logging.

HostedZoneId (string) --The ID of the hosted zone that CloudWatch Logs is logging queries for.

CloudWatchLogsLogGroupArn (string) --The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.








Exceptions

Route53.Client.exceptions.NoSuchQueryLoggingConfig
Route53.Client.exceptions.InvalidInput


    :return: {
        'QueryLoggingConfig': {
            'Id': 'string',
            'HostedZoneId': 'string',
            'CloudWatchLogsLogGroupArn': 'string'
        }
    }
    
    
    """
    pass

def get_reusable_delegation_set(Id=None):
    """
    Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reusable_delegation_set(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the reusable delegation set that you want to get a list of name servers for.\n

    :rtype: dict
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

CallerReference (string) --The value that you specified for CallerReference when you created the reusable delegation set.

NameServers (list) --A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string) --









Exceptions

Route53.Client.exceptions.NoSuchDelegationSet
Route53.Client.exceptions.DelegationSetNotReusable
Route53.Client.exceptions.InvalidInput


    :return: {
        'DelegationSet': {
            'Id': 'string',
            'CallerReference': 'string',
            'NameServers': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchDelegationSet
    Route53.Client.exceptions.DelegationSetNotReusable
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def get_reusable_delegation_set_limit(Type=None, DelegationSetId=None):
    """
    Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.
    For the default limit, see Limits in the Amazon Route 53 Developer Guide . To request a higher limit, open a case .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reusable_delegation_set_limit(
        Type='MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
        DelegationSetId='string'
    )
    
    
    :type Type: string
    :param Type: [REQUIRED]\nSpecify MAX_ZONES_BY_REUSABLE_DELEGATION_SET to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.\n

    :type DelegationSetId: string
    :param DelegationSetId: [REQUIRED]\nThe ID of the delegation set that you want to get the limit for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Limit': {
        'Type': 'MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
        'Value': 123
    },
    'Count': 123
}


Response Structure

(dict) --
A complex type that contains the requested limit.

Limit (dict) --
The current setting for the limit on hosted zones that you can associate with the specified reusable delegation set.

Type (string) --
The limit that you requested: MAX_ZONES_BY_REUSABLE_DELEGATION_SET , the maximum number of hosted zones that you can associate with the specified reusable delegation set.

Value (integer) --
The current value for the MAX_ZONES_BY_REUSABLE_DELEGATION_SET limit.



Count (integer) --
The current number of hosted zones that you can associate with the specified reusable delegation set.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchDelegationSet


    :return: {
        'Limit': {
            'Type': 'MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
            'Value': 123
        },
        'Count': 123
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchDelegationSet
    
    """
    pass

def get_traffic_policy(Id=None, Version=None):
    """
    Gets information about a specific traffic policy version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_traffic_policy(
        Id='string',
        Version=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy that you want to get information about.\n

    :type Version: integer
    :param Version: [REQUIRED]\nThe version number of the traffic policy that you want to get information about.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicy': {
        'Id': 'string',
        'Version': 123,
        'Name': 'string',
        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'Document': 'string',
        'Comment': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicy (dict) --
A complex type that contains settings for the specified traffic policy.

Id (string) --
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

Version (integer) --
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of Version is always 1.

Name (string) --
The name that you specified when you created the traffic policy.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

Document (string) --
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the CreateTrafficPolicy request. For more information about the JSON format, see Traffic Policy Document Format .

Comment (string) --
The comment that you specify in the CreateTrafficPolicy request, if any.









Exceptions

Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.InvalidInput


    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'Document': 'string',
            'Comment': 'string'
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchTrafficPolicy
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def get_traffic_policy_instance(Id=None):
    """
    Gets information about a specified traffic policy instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_traffic_policy_instance(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy instance that you want to get information about.\n

    :rtype: dict
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
        'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
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
Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating
Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed
Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.








Exceptions

Route53.Client.exceptions.NoSuchTrafficPolicyInstance
Route53.Client.exceptions.InvalidInput


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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
        }
    }
    
    
    """
    pass

def get_traffic_policy_instance_count():
    """
    Gets the number of traffic policy instances that are associated with the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_traffic_policy_instance_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'TrafficPolicyInstanceCount': 123
}


Response Structure

(dict) --A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.

TrafficPolicyInstanceCount (integer) --The number of traffic policy instances that are associated with the current AWS account.







    :return: {
        'TrafficPolicyInstanceCount': 123
    }
    
    
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

def list_geo_locations(StartContinentCode=None, StartCountryCode=None, StartSubdivisionCode=None, MaxItems=None):
    """
    Retrieves a list of supported geographic locations.
    Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.
    For a list of supported geolocation codes, see the GeoLocation data type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_geo_locations(
        StartContinentCode='string',
        StartCountryCode='string',
        StartSubdivisionCode='string',
        MaxItems='string'
    )
    
    
    :type StartContinentCode: string
    :param StartContinentCode: The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if IsTruncated is true, and if NextContinentCode from the previous response has a value, enter that value in startcontinentcode to return the next page of results.\nInclude startcontinentcode only if you want to list continents. Don\'t include startcontinentcode when you\'re listing countries or countries with their subdivisions.\n

    :type StartCountryCode: string
    :param StartCountryCode: The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextCountryCode from the previous response has a value, enter that value in startcountrycode to return the next page of results.

    :type StartSubdivisionCode: string
    :param StartSubdivisionCode: The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if IsTruncated is true , and if NextSubdivisionCode from the previous response has a value, enter that value in startsubdivisioncode to return the next page of results.\nTo list subdivisions (U.S. states), you must include both startcountrycode and startsubdivisioncode .\n

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of geolocations to be included in the response body for this request. If more than maxitems geolocations remain to be listed, then the value of the IsTruncated element in the response is true .

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
A complex type containing the response information for the request.

GeoLocationDetailsList (list) --
A complex type that contains one GeoLocationDetails element for each location that Amazon Route 53 supports for geolocation.

(dict) --
A complex type that contains the codes and full continent, country, and subdivision names for the specified geolocation code.

ContinentCode (string) --
The two-letter code for the continent.

ContinentName (string) --
The full name of the continent.

CountryCode (string) --
The two-letter code for the country.

CountryName (string) --
The name of the country.

SubdivisionCode (string) --
The code for the subdivision. Route 53 currently supports only states in the United States.

SubdivisionName (string) --
The full name of the subdivision. Route 53 currently supports only states in the United States.





IsTruncated (boolean) --
A value that indicates whether more locations remain to be listed after the last location in this response. If so, the value of IsTruncated is true . To get more values, submit another request and include the values of NextContinentCode , NextCountryCode , and NextSubdivisionCode in the startcontinentcode , startcountrycode , and startsubdivisioncode , as applicable.

NextContinentCode (string) --
If IsTruncated is true , you can make a follow-up request to display more locations. Enter the value of NextContinentCode in the startcontinentcode parameter in another ListGeoLocations request.

NextCountryCode (string) --
If IsTruncated is true , you can make a follow-up request to display more locations. Enter the value of NextCountryCode in the startcountrycode parameter in another ListGeoLocations request.

NextSubdivisionCode (string) --
If IsTruncated is true , you can make a follow-up request to display more locations. Enter the value of NextSubdivisionCode in the startsubdivisioncode parameter in another ListGeoLocations request.

MaxItems (string) --
The value that you specified for MaxItems in the request.







Exceptions

Route53.Client.exceptions.InvalidInput


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
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def list_health_checks(Marker=None, MaxItems=None):
    """
    Retrieve a list of the health checks that are associated with the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_health_checks(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: If the value of IsTruncated in the previous response was true , you have more health checks. To get another group, submit another ListHealthChecks request.\nFor the value of marker , specify the value of NextMarker from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more health checks to get.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of health checks that you want ListHealthChecks to return in response to the current request. Amazon Route 53 returns a maximum of 100 items. If you set MaxItems to a value greater than 100, Route 53 returns only the first 100 health checks.

    :rtype: dict

ReturnsResponse Syntax
{
    'HealthChecks': [
        {
            'Id': 'string',
            'CallerReference': 'string',
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            },
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
                'Disabled': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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


Response Structure

(dict) --
A complex type that contains the response to a ListHealthChecks request.

HealthChecks (list) --
A complex type that contains one HealthCheck element for each health check that is associated with the current AWS account.

(dict) --
A complex type that contains information about one health check that is associated with the current AWS account.

Id (string) --
The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

CallerReference (string) --
A unique string that you specified when you created the health check.

LinkedService (dict) --
If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can\'t edit or delete it using Amazon Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.



HealthCheckConfig (dict) --
A complex type that contains detailed information about one health check.

IPAddress (string) --
The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
Use one of the following formats for the value of IPAddress :

IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .

If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
For more information, see FullyQualifiedDomainName .
Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:

RFC 5735, Special Use IPv4 Addresses
RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
RFC 5156, Special-Use IPv6 Addresses

When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .

Port (integer) --
The port on the endpoint that you want Amazon Route 53 to perform health checks on.

Note
Don\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .


Type (string) --
The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

Warning
You can\'t change the value of Type after you create a health check.

You can create the following types of health checks:

HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.


Warning
If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.


HTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
HTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
TCP : Route 53 tries to establish a TCP connection.
CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
CALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .

For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .

ResourcePath (string) --
The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .

FullyQualifiedDomainName (string) --
Amazon Route 53 behavior depends on whether you specify a value for IPAddress .

If you specify a value for IPAddress :

Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
When Route 53 checks the health of an endpoint, here is how it constructs the Host header:

If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.

If you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.

**If you don\'t specify a value for IPAddress ** :

Route 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

Note
If you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a "DNS resolution failed" error.

If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

Warning
In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.

SearchString (string) --
If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
Route 53 considers case when searching for SearchString in the response body.

RequestInterval (integer) --
The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.

Warning
You can\'t change the value of RequestInterval after you create a health check.

If you don\'t specify a value for RequestInterval , the default value is 30 seconds.

FailureThreshold (integer) --
The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
If you don\'t specify a value for FailureThreshold , the default value is three health checks.

MeasureLatency (boolean) --
Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.

Warning
You can\'t change the value of MeasureLatency after you create a health check.


Inverted (boolean) --
Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

Disabled (boolean) --
Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:

Health checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.
Calculated health checks: Route 53 stops aggregating the status of the referenced health checks.
Health checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.

After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .
Charges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .

HealthThreshold (integer) --
The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.
Note the following:

If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
If you specify 0 , Route 53 always considers this health check to be healthy.


ChildHealthChecks (list) --
(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.

(string) --


EnableSNI (boolean) --
Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.

Regions (list) --
A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .
If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

(string) --


AlarmIdentifier (dict) --
A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

Region (string) --
For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
For the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .

Name (string) --
The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

Note
Route 53 supports CloudWatch alarms with the following features:

Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.





InsufficientDataHealthStatus (string) --
When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

Healthy : Route 53 considers the health check to be healthy.
Unhealthy : Route 53 considers the health check to be unhealthy.
LastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.




HealthCheckVersion (integer) --
The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.

CloudWatchAlarmConfiguration (dict) --
A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

EvaluationPeriods (integer) --
For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

Threshold (float) --
For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

ComparisonOperator (string) --
For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

Period (integer) --
For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

MetricName (string) --
The name of the CloudWatch metric that the alarm is associated with.

Namespace (string) --
The namespace of the metric that the alarm is associated with. For more information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

Statistic (string) --
For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

Dimensions (list) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

(dict) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

Name (string) --
For the metric that the CloudWatch alarm is associated with, the name of one dimension.

Value (string) --
For the metric that the CloudWatch alarm is associated with, the value of one dimension.











Marker (string) --
For the second and subsequent calls to ListHealthChecks , Marker is the value that you specified for the marker parameter in the previous request.

IsTruncated (boolean) --
A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another ListHealthChecks request and specifying the value of NextMarker in the marker parameter.

NextMarker (string) --
If IsTruncated is true , the value of NextMarker identifies the first health check that Amazon Route 53 returns if you submit another ListHealthChecks request and specify the value of NextMarker in the marker parameter.

MaxItems (string) --
The value that you specified for the maxitems parameter in the call to ListHealthChecks that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.IncompatibleVersion


    :return: {
        'HealthChecks': [
            {
                'Id': 'string',
                'CallerReference': 'string',
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                },
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
                    'Disabled': True|False,
                    'HealthThreshold': 123,
                    'ChildHealthChecks': [
                        'string',
                    ],
                    'EnableSNI': True|False,
                    'Regions': [
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                    ],
                    'AlarmIdentifier': {
                        'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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
    IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
    IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .
    
    """
    pass

def list_hosted_zones(Marker=None, MaxItems=None, DelegationSetId=None):
    """
    Retrieves a list of the public and private hosted zones that are associated with the current AWS account. The response includes a HostedZones child element for each hosted zone.
    Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the maxitems parameter to list them in groups of up to 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hosted_zones(
        Marker='string',
        MaxItems='string',
        DelegationSetId='string'
    )
    
    
    :type Marker: string
    :param Marker: If the value of IsTruncated in the previous response was true , you have more hosted zones. To get more hosted zones, submit another ListHostedZones request.\nFor the value of marker , specify the value of NextMarker from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more hosted zones to get.\n

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than maxitems hosted zones, the value of IsTruncated in the response is true , and the value of NextMarker is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.

    :type DelegationSetId: string
    :param DelegationSetId: If you\'re using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZones': [
        {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
        },
    ],
    'Marker': 'string',
    'IsTruncated': True|False,
    'NextMarker': 'string',
    'MaxItems': 'string'
}


Response Structure

(dict) --

HostedZones (list) --
A complex type that contains general information about the hosted zone.

(dict) --
A complex type that contains general information about the hosted zone.

Id (string) --
The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name (string) --
The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .

CallerReference (string) --
The value that you specified for CallerReference when you created the hosted zone.

Config (dict) --
A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don\'t appear in the response.

Comment (string) --
Any comments that you want to include about the hosted zone.

PrivateZone (boolean) --
A value that indicates whether this is a private hosted zone.



ResourceRecordSetCount (integer) --
The number of resource record sets in the hosted zone.

LinkedService (dict) --
If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.







Marker (string) --
For the second and subsequent calls to ListHostedZones , Marker is the value that you specified for the marker parameter in the request that produced the current response.

IsTruncated (boolean) --
A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another ListHostedZones request and specifying the value of NextMarker in the marker parameter.

NextMarker (string) --
If IsTruncated is true , the value of NextMarker identifies the first hosted zone in the next group of hosted zones. Submit another ListHostedZones request, and specify the value of NextMarker from the response in the marker parameter.
This element is present only if IsTruncated is true .

MaxItems (string) --
The value that you specified for the maxitems parameter in the call to ListHostedZones that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchDelegationSet
Route53.Client.exceptions.DelegationSetNotReusable


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
                'ResourceRecordSetCount': 123,
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                }
            },
        ],
        'Marker': 'string',
        'IsTruncated': True|False,
        'NextMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchDelegationSet
    Route53.Client.exceptions.DelegationSetNotReusable
    
    """
    pass

def list_hosted_zones_by_name(DNSName=None, HostedZoneId=None, MaxItems=None):
    """
    Retrieves a list of your hosted zones in lexicographic order. The response includes a HostedZones child element for each hosted zone created by the current AWS account.
    Note the trailing dot, which can change the sort order in some circumstances.
    If the domain name includes escape characters or Punycode, ListHostedZonesByName alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for ex\xc3\xa4mple.com, you specify ex344mple.com for the domain name. ListHostedZonesByName alphabetizes it as:
    The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
    Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the MaxItems parameter to list them in groups of up to 100. The response includes values that help navigate from one group of MaxItems hosted zones to the next:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hosted_zones_by_name(
        DNSName='string',
        HostedZoneId='string',
        MaxItems='string'
    )
    
    
    :type DNSName: string
    :param DNSName: (Optional) For your first request to ListHostedZonesByName , include the dnsname parameter only if you want to specify the name of the first hosted zone in the response. If you don\'t include the dnsname parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both dnsname and hostedzoneid parameters. For dnsname , specify the value of NextDNSName from the previous response.

    :type HostedZoneId: string
    :param HostedZoneId: (Optional) For your first request to ListHostedZonesByName , do not include the hostedzoneid parameter.\nIf you have more hosted zones than the value of maxitems , ListHostedZonesByName returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZonesByName and include both dnsname and hostedzoneid parameters. For the value of hostedzoneid , specify the value of the NextHostedZoneId element from the previous response.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, then the value of the IsTruncated element in the response is true, and the values of NextDNSName and NextHostedZoneId specify the first hosted zone in the next group of maxitems hosted zones.

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZones': [
        {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
        },
    ],
    'DNSName': 'string',
    'HostedZoneId': 'string',
    'IsTruncated': True|False,
    'NextDNSName': 'string',
    'NextHostedZoneId': 'string',
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

HostedZones (list) --
A complex type that contains general information about the hosted zone.

(dict) --
A complex type that contains general information about the hosted zone.

Id (string) --
The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name (string) --
The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .

CallerReference (string) --
The value that you specified for CallerReference when you created the hosted zone.

Config (dict) --
A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don\'t appear in the response.

Comment (string) --
Any comments that you want to include about the hosted zone.

PrivateZone (boolean) --
A value that indicates whether this is a private hosted zone.



ResourceRecordSetCount (integer) --
The number of resource record sets in the hosted zone.

LinkedService (dict) --
If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.







DNSName (string) --
For the second and subsequent calls to ListHostedZonesByName , DNSName is the value that you specified for the dnsname parameter in the request that produced the current response.

HostedZoneId (string) --
The ID that Amazon Route 53 assigned to the hosted zone when you created it.

IsTruncated (boolean) --
A flag that indicates whether there are more hosted zones to be listed. If the response was truncated, you can get the next group of maxitems hosted zones by calling ListHostedZonesByName again and specifying the values of NextDNSName and NextHostedZoneId elements in the dnsname and hostedzoneid parameters.

NextDNSName (string) --
If IsTruncated is true, the value of NextDNSName is the name of the first hosted zone in the next group of maxitems hosted zones. Call ListHostedZonesByName again and specify the value of NextDNSName and NextHostedZoneId in the dnsname and hostedzoneid parameters, respectively.
This element is present only if IsTruncated is true .

NextHostedZoneId (string) --
If IsTruncated is true , the value of NextHostedZoneId identifies the first hosted zone in the next group of maxitems hosted zones. Call ListHostedZonesByName again and specify the value of NextDNSName and NextHostedZoneId in the dnsname and hostedzoneid parameters, respectively.
This element is present only if IsTruncated is true .

MaxItems (string) --
The value that you specified for the maxitems parameter in the call to ListHostedZonesByName that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.InvalidDomainName


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
                'ResourceRecordSetCount': 123,
                'LinkedService': {
                    'ServicePrincipal': 'string',
                    'Description': 'string'
                }
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
    DNSName (string) -- (Optional) For your first request to ListHostedZonesByName , include the dnsname parameter only if you want to specify the name of the first hosted zone in the response. If you don\'t include the dnsname parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both dnsname and hostedzoneid parameters. For dnsname , specify the value of NextDNSName from the previous response.
    HostedZoneId (string) -- (Optional) For your first request to ListHostedZonesByName , do not include the hostedzoneid parameter.
    If you have more hosted zones than the value of maxitems , ListHostedZonesByName returns only the first maxitems hosted zones. To get the next group of maxitems hosted zones, submit another request to ListHostedZonesByName and include both dnsname and hostedzoneid parameters. For the value of hostedzoneid , specify the value of the NextHostedZoneId element from the previous response.
    
    MaxItems (string) -- The maximum number of hosted zones to be included in the response body for this request. If you have more than maxitems hosted zones, then the value of the IsTruncated element in the response is true, and the values of NextDNSName and NextHostedZoneId specify the first hosted zone in the next group of maxitems hosted zones.
    
    """
    pass

def list_query_logging_configs(HostedZoneId=None, NextToken=None, MaxResults=None):
    """
    Lists the configurations for DNS query logging that are associated with the current AWS account or the configuration that is associated with a specified hosted zone.
    For more information about DNS query logs, see CreateQueryLoggingConfig . Additional information, including the format of DNS query logs, appears in Logging DNS Queries in the Amazon Route 53 Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_query_logging_configs(
        HostedZoneId='string',
        NextToken='string',
        MaxResults='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: (Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in HostedZoneId .\nIf you don\'t specify a hosted zone ID, ListQueryLoggingConfigs returns all of the configurations that are associated with the current AWS account.\n

    :type NextToken: string
    :param NextToken: (Optional) If the current AWS account has more than MaxResults query logging configurations, use NextToken to get the second and subsequent pages of results.\nFor the first ListQueryLoggingConfigs request, omit this value.\nFor the second and subsequent requests, get the value of NextToken from the previous response and specify that value for NextToken in the request.\n

    :type MaxResults: string
    :param MaxResults: (Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current AWS account has more than MaxResults configurations, use the value of NextToken in the response to get the next page of results.\nIf you don\'t specify a value for MaxResults , Route 53 returns up to 100 configurations.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'QueryLoggingConfigs': [
        {
            'Id': 'string',
            'HostedZoneId': 'string',
            'CloudWatchLogsLogGroupArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

QueryLoggingConfigs (list) --
An array that contains one QueryLoggingConfig element for each configuration for DNS query logging that is associated with the current AWS account.

(dict) --
A complex type that contains information about a configuration for DNS query logging.

Id (string) --
The ID for a configuration for DNS query logging.

HostedZoneId (string) --
The ID of the hosted zone that CloudWatch Logs is logging queries for.

CloudWatchLogsLogGroupArn (string) --
The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.





NextToken (string) --
If a response includes the last of the query logging configurations that are associated with the current AWS account, NextToken doesn\'t appear in the response.
If a response doesn\'t include the last of the configurations, you can get more configurations by submitting another ListQueryLoggingConfigs request. Get the value of NextToken that Amazon Route 53 returned in the previous response and include it in NextToken in the next request.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.InvalidPaginationToken
Route53.Client.exceptions.NoSuchHostedZone


    :return: {
        'QueryLoggingConfigs': [
            {
                'Id': 'string',
                'HostedZoneId': 'string',
                'CloudWatchLogsLogGroupArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.InvalidPaginationToken
    Route53.Client.exceptions.NoSuchHostedZone
    
    """
    pass

def list_resource_record_sets(HostedZoneId=None, StartRecordName=None, StartRecordType=None, StartRecordIdentifier=None, MaxItems=None):
    """
    Lists the resource record sets in a specified hosted zone.
    Note the trailing dot, which can change the sort order when the record name contains characters that appear before . (decimal 46) in the ASCII table. These characters include the following: ! " # $ % & \' ( ) * + , -
    When multiple records have the same DNS name, ListResourceRecordSets sorts results by the record type.
    You can use the name and type elements to specify the resource record set that the list begins with:
    The results begin with the first resource record set that the hosted zone contains.
    The results begin with the first resource record set in the list whose name is greater than or equal to Name .
    Amazon Route 53 returns the InvalidInput error.
    The results begin with the first resource record set in the list whose name is greater than or equal to Name , and whose type is greater than or equal to Type .
    This action returns the most current version of the records. This includes records that are PENDING , and that are not yet available on all Route 53 DNS servers.
    To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a ChangeResourceRecordSets request while you\'re paging through the results of a ListResourceRecordSets request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.
    If a ListResourceRecordSets command returns more than one page of results, the value of IsTruncated is true . To display the next page of results, get the values of NextRecordName , NextRecordType , and NextRecordIdentifier (if any) from the response. Then submit another ListResourceRecordSets request, and specify those values for StartRecordName , StartRecordType , and StartRecordIdentifier .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_record_sets(
        HostedZoneId='string',
        StartRecordName='string',
        StartRecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        StartRecordIdentifier='string',
        MaxItems='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that contains the resource record sets that you want to list.\n

    :type StartRecordName: string
    :param StartRecordName: The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn\'t exist, the results begin with the first resource record set that has a name greater than the value of name .

    :type StartRecordType: string
    :param StartRecordType: The type of resource record set to begin the record listing from.\nValid values for basic resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT\nValues for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT\nValues for alias resource record sets:\n\nAPI Gateway custom regional API or edge-optimized API : A\nCloudFront distribution : A or AAAA\nElastic Beanstalk environment that has a regionalized subdomain : A\nElastic Load Balancing load balancer : A | AAAA\nS3 bucket : A\nVPC interface VPC endpoint : A\nAnother resource record set in this hosted zone: The type of the resource record set that the alias references.\n\nConstraint: Specifying type without specifying name returns an InvalidInput error.\n

    :type StartRecordIdentifier: string
    :param StartRecordIdentifier: Resource record sets that have a routing policy other than simple: If results were truncated for a given DNS name and type, specify the value of NextRecordIdentifier from the previous response to get the next resource record set that has the current DNS name and type.

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than maxitems resource record sets, the value of the IsTruncated element in the response is true , and the values of the NextRecordName and NextRecordType elements in the response identify the first resource record set in the next group of maxitems resource record sets.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceRecordSets': [
        {
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'SetIdentifier': 'string',
            'Weight': 123,
            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-north-1'|'cn-northwest-1'|'ap-east-1'|'me-south-1'|'ap-south-1'|'af-south-1'|'eu-south-1',
            'GeoLocation': {
                'ContinentCode': 'string',
                'CountryCode': 'string',
                'SubdivisionCode': 'string'
            },
            'Failover': 'PRIMARY'|'SECONDARY',
            'MultiValueAnswer': True|False,
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
    'NextRecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
    'NextRecordIdentifier': 'string',
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains list information for the resource record set.

ResourceRecordSets (list) --
Information about multiple resource record sets.

(dict) --
Information about the resource record set to create or delete.

Name (string) --
For ChangeResourceRecordSets requests, the name of the record that you want to create, update, or delete. For ListResourceRecordSets responses, the name of a record in the specified hosted zone.

ChangeResourceRecordSets Only

Enter a fully qualified domain name, for example, www.example.com . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see DNS Domain Name Format in the Amazon Route 53 Developer Guide .
You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, *.example.com . Note the following:

The * must replace the entire label. For example, you can\'t specify *prod.example.com or prod*.example.com .
The * can\'t replace any of the middle labels, for example, marketing.*.example.com.
If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.


Warning
You can\'t use the * wildcard for resource records sets that have a type of NS.

You can use the * wildcard as the leftmost label in a domain name, for example, *.example.com . You can\'t use an * for one of the middle labels, for example, marketing.*.example.com . In addition, the * must replace the entire label; for example, you can\'t specify prod*.example.com .

Type (string) --
The DNS record type. For information about different record types and how data is encoded for them, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
Valid values for basic resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | NS | PTR | SOA | SPF | SRV | TXT
Values for weighted, latency, geolocation, and failover resource record sets: A | AAAA | CAA | CNAME | MX | NAPTR | PTR | SPF | SRV | TXT . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
Valid values for multivalue answer resource record sets: A | AAAA | MX | NAPTR | PTR | SPF | SRV | TXT

Note
SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of Type is SPF . RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1 , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, The SPF DNS Record Type .

Values for alias resource record sets:

Amazon API Gateway custom regional APIs and edge-optimized APIs: A
CloudFront distributions: A   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of A and one with a value of AAAA .
Amazon API Gateway environment that has a regionalized subdomain : A
ELB load balancers: A | AAAA
Amazon S3 buckets: A
Amazon Virtual Private Cloud interface VPC endpoints A
Another resource record set in this hosted zone: Specify the type of the resource record set that you\'re creating the alias for. All values are supported except NS and SOA .


Note
If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t route traffic to a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.


SetIdentifier (string) --

Resource record sets that have a routing policy other than simple: An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of SetIdentifier must be unique for each resource record set.

For information about routing policies, see Choosing a Routing Policy in the Amazon Route 53 Developer Guide .

Weight (integer) --

Weighted resource record sets only: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource\'s weight to the total. Note the following:


You must specify a value for the Weight element for every weighted resource record set.
You can only specify one ResourceRecord per weighted resource record set.
You can\'t create latency, failover, or geolocation resource record sets that have the same values for the Name and Type elements as weighted resource record sets.
You can create a maximum of 100 weighted resource record sets that have the same values for the Name and Type elements.
For weighted (but not weighted alias) resource record sets, if you set Weight to 0 for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set Weight to 0 for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting Weight to 0 is different when you associate health checks with weighted resource record sets. For more information, see Options for Configuring Route 53 Active-Active and Active-Passive Failover in the Amazon Route 53 Developer Guide .


Region (string) --

Latency-based resource record sets only: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.


Note
Although creating latency and latency alias resource record sets in a private hosted zone is allowed, it\'s not supported.

When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.
Note the following:

You can only specify one ResourceRecord per latency resource record set.
You can only create one latency resource record set for each Amazon EC2 Region.
You aren\'t required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.
You can\'t create non-latency resource record sets that have the same values for the Name and Type elements as latency resource record sets.


GeoLocation (dict) --

Geolocation resource record sets only: A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of 192.0.2.111 , create a resource record set with a Type of A and a ContinentCode of AF .


Note
Although creating geolocation and geolocation alias resource record sets in a private hosted zone is allowed, it\'s not supported.

If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
You can\'t create two geolocation resource record sets that specify the same geographic location.
The value * in the CountryCode element matches all geographic locations that aren\'t specified in other geolocation resource record sets that have the same values for the Name and Type elements.

Warning
Geolocation works by mapping IP addresses to locations. However, some IP addresses aren\'t mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can\'t identify. We recommend that you create a resource record set for which the value of CountryCode is * . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven\'t created geolocation resource record sets and queries from IP addresses that aren\'t mapped to a location. If you don\'t create a * resource record set, Route 53 returns a "no answer" response for queries from those locations.

You can\'t create non-geolocation resource record sets that have the same values for the Name and Type elements as geolocation resource record sets.

ContinentCode (string) --
The two-letter code for the continent.
Amazon Route 53 supports the following continent codes:

AF : Africa
AN : Antarctica
AS : Asia
EU : Europe
OC : Oceania
NA : North America
SA : South America

Constraint: Specifying ContinentCode with either CountryCode or SubdivisionCode returns an InvalidInput error.

CountryCode (string) --
For geolocation resource record sets, the two-letter code for a country.
Amazon Route 53 uses the two-letter country codes that are specified in ISO standard 3166-1 alpha-2 .

SubdivisionCode (string) --
For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn\'t support any other values for SubdivisionCode . For a list of state abbreviations, see Appendix B: Two\xe2\x80\x93Letter State and Possession Abbreviations on the United States Postal Service website.
If you specify subdivisioncode , you must also specify US for CountryCode .



Failover (string) --

Failover resource record sets only: To configure failover, you add the Failover element to two resource record sets. For one resource record set, you specify PRIMARY as the value for Failover ; for the other resource record set, you specify SECONDARY . In addition, you include the HealthCheckId element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

Except where noted, the following failover behaviors assume that you have included the HealthCheckId element in both resource record sets:

When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
If you omit the HealthCheckId element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.

You can\'t create non-failover resource record sets that have the same values for the Name and Type elements as failover resource record sets.
For failover alias resource record sets, you must also include the EvaluateTargetHealth element and set the value to true.
For more information about configuring failover for Route 53, see the following topics in the Amazon Route 53 Developer Guide :

Route 53 Health Checks and DNS Failover
Configuring Failover in a Private Hosted Zone


MultiValueAnswer (boolean) --

Multivalue answer resource record sets only : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify true for MultiValueAnswer . Note the following:


If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.
If you don\'t associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.
Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.
If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.
When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.
If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.

You can\'t create multivalue answer alias records.

TTL (integer) --
The resource record cache time to live (TTL), in seconds. Note the following:

If you\'re creating or updating an alias resource record set, omit TTL . Amazon Route 53 uses the value of TTL for the alias target.
If you\'re associating this resource record set with a health check (if you\'re adding a HealthCheckId element), we recommend that you specify a TTL of 60 seconds or less so clients respond quickly to changes in health status.
All of the resource record sets in a group of weighted resource record sets must have the same value for TTL .
If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a TTL of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for Weight .


ResourceRecords (list) --
Information about the resource records to act upon.

Note
If you\'re creating an alias resource record set, omit ResourceRecords .


(dict) --
Information specific to the resource record.

Note
If you\'re creating an alias resource record set, omit ResourceRecord .


Value (string) --
The current or new DNS record value, not to exceed 4,000 characters. In the case of a DELETE action, if the current value does not match the actual value, an error is returned. For descriptions about how to format Value for different record types, see Supported DNS Resource Record Types in the Amazon Route 53 Developer Guide .
You can specify more than one value for all record types except CNAME and SOA .

Note
If you\'re creating an alias resource record set, omit Value .






AliasTarget (dict) --

Alias resource record sets only: Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

If you\'re creating resource records sets for a private hosted zone, note the following:

You can\'t create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.
Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported.
For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone in the Amazon Route 53 Developer Guide .


HostedZoneId (string) --

Alias resource records sets only : The value used depends on where you want to route traffic:

Amazon API Gateway custom regional APIs and edge-optimized APIs


Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command get-domain-names :

For regional APIs, specify the value of regionalHostedZoneId .

For edge-optimized APIs, specify the value of distributionHostedZoneId .
Amazon Virtual Private Cloud interface VPC endpoint


Specify the hosted zone ID for your interface endpoint. You can get the value of HostedZoneId using the AWS CLI command describe-vpc-endpoints .

CloudFront distribution

Specify Z2FDTNDATAQYW2 .

Note
Alias resource record sets for CloudFront can\'t be created in a private zone.
Elastic Beanstalk environment

Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see AWS Elastic Beanstalk in the "AWS Service Endpoints" chapter of the Amazon Web Services General Reference .

ELB load balancer

Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:

Service Endpoints table in the "Elastic Load Balancing Endpoints and Quotas" topic in the Amazon Web Services General Reference : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.

AWS Management Console : Go to the Amazon EC2 page, choose Load Balancers in the navigation pane, select the load balancer, and get the value of the Hosted zone field on the Description tab.

Elastic Load Balancing API : Use DescribeLoadBalancers to get the applicable value. For more information, see the applicable guide:

Classic Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneNameId .
Application and Network Load Balancers: Use DescribeLoadBalancers to get the value of CanonicalHostedZoneId .


AWS CLI : Use describe-load-balancers to get the applicable value. For more information, see the applicable guide:

Classic Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneNameId .
Application and Network Load Balancers: Use describe-load-balancers to get the value of CanonicalHostedZoneId .

AWS Global Accelerator accelerator


Specify Z2BJ6XQ5FK7U4H .

An Amazon S3 bucket configured as a static website

Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference .

Another Route 53 resource record set in your hosted zone

Specify the hosted zone ID of your hosted zone. (An alias resource record set can\'t reference a resource record set in a different hosted zone.)

DNSName (string) --

Alias resource record sets only: The value that you specify depends on where you want to route queries:

Amazon API Gateway custom regional APIs and edge-optimized APIs


Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command get-domain-names :

For regional APIs, specify the value of regionalDomainName .
For edge-optimized APIs, specify the value of distributionDomainName . This is the name of the associated CloudFront distribution, such as da1b2c3d4e5.cloudfront.net .


Note
The name of the record that you\'re creating must match a custom domain name for your API, such as api.example.com .
Amazon Virtual Private Cloud interface VPC endpoint

Enter the API endpoint for the interface endpoint, such as vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of DnsName using the AWS CLI command describe-vpc-endpoints .

CloudFront distribution

Specify the domain name that CloudFront assigned when you created your distribution.
Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is acme.example.com , your CloudFront distribution must include acme.example.com as one of the alternate domain names. For more information, see Using Alternate Domain Names (CNAMEs) in the Amazon CloudFront Developer Guide .
You can\'t create a resource record set in a private hosted zone to route traffic to a CloudFront distribution.

Note
For failover alias records, you can\'t specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can\'t include the same alternate domain name in more than one distribution.
Elastic Beanstalk environment

If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name my-environment.*us-west-2* .elasticbeanstalk.com is a regionalized domain name.

Warning
For environments that were created before early 2016, the domain name doesn\'t include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can\'t create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can\'t create a record that routes traffic for example.com to your Elastic Beanstalk environment.

For Elastic Beanstalk environments that have regionalized subdomains, specify the CNAME attribute for the environment. You can use the following methods to get the value of the CNAME attribute:

AWS Management Console : For information about how to get the value by using the console, see Using Custom Domains with AWS Elastic Beanstalk in the AWS Elastic Beanstalk Developer Guide .

Elastic Beanstalk API : Use the DescribeEnvironments action to get the value of the CNAME attribute. For more information, see DescribeEnvironments in the AWS Elastic Beanstalk API Reference .

AWS CLI : Use the describe-environments command to get the value of the CNAME attribute. For more information, see describe-environments in the AWS CLI Command Reference .
ELB load balancer


Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI.

AWS Management Console : Go to the EC2 page, choose Load Balancers in the navigation pane, choose the load balancer, choose the Description tab, and get the value of the DNS name field.  If you\'re routing traffic to a Classic Load Balancer, get the value that begins with dualstack . If you\'re routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.

Elastic Load Balancing API : Use DescribeLoadBalancers to get the value of DNSName . For more information, see the applicable guide:

Classic Load Balancers: DescribeLoadBalancers
Application and Network Load Balancers: DescribeLoadBalancers


AWS CLI : Use describe-load-balancers to get the value of DNSName . For more information, see the applicable guide:

Classic Load Balancers: describe-load-balancers
Application and Network Load Balancers: describe-load-balancers

AWS Global Accelerator accelerator


Specify the DNS name for your accelerator:

Global Accelerator API: To get the DNS name, use DescribeAccelerator .

AWS CLI: To get the DNS name, use describe-accelerator .
Amazon S3 bucket that is configured as a static website


Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, s3-website.us-east-2.amazonaws.com . For more information about valid values, see the table Amazon S3 Website Endpoints in the Amazon Web Services General Reference . For more information about using S3 buckets for websites, see Getting Started with Amazon Route 53 in the Amazon Route 53 Developer Guide.

Another Route 53 resource record set

Specify the value of the Name element for a resource record set in the current hosted zone.

Note
If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t specify the domain name for a record for which the value of Type is CNAME . This is because the alias record must have the same type as the record that you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.


EvaluateTargetHealth (boolean) --

Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets: When EvaluateTargetHealth is true , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone.

Note the following:

CloudFront distributions

You can\'t set EvaluateTargetHealth to true when the alias target is a CloudFront distribution.

Elastic Beanstalk environments that have regionalized subdomains

If you specify an Elastic Beanstalk environment in DNSName and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set EvaluateTargetHealth to true and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.
If the environment contains a single Amazon EC2 instance, there are no special requirements.

ELB load balancers

Health checking behavior depends on the type of load balancer:

Classic Load Balancers : If you specify an ELB Classic Load Balancer in DNSName , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set EvaluateTargetHealth to true and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.
Application and Network Load Balancers : If you specify an ELB Application or Network Load Balancer and you set EvaluateTargetHealth to true , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:
For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.
A target group that has no registered targets is considered unhealthy.




Note
When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they\'re not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.
S3 buckets

There are no special requirements for setting EvaluateTargetHealth to true when the alias target is an S3 bucket.

Other records in the same hosted zone

If the AWS resource that you specify in DNSName is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see What Happens When You Omit Health Checks? in the Amazon Route 53 Developer Guide .
For more information and examples, see Amazon Route 53 Health Checks and DNS Failover in the Amazon Route 53 Developer Guide .



HealthCheckId (string) --
If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the HealthCheckId element and specify the ID of the applicable health check.
Route 53 determines whether a resource record set is healthy based on one of the following:

By periodically sending a request to the endpoint that is specified in the health check
By aggregating the status of a specified group of health checks (calculated health checks)
By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)


Warning
Route 53 doesn\'t check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the Value element. When you add a HealthCheckId element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.

For more information, see the following topics in the Amazon Route 53 Developer Guide :

How Amazon Route 53 Determines Whether an Endpoint Is Healthy
Route 53 Health Checks and DNS Failover
Configuring Failover in a Private Hosted Zone


When to Specify HealthCheckId

Specifying a value for HealthCheckId is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:

Non-alias resource record sets : You\'re checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.  If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.
Alias resource record sets : You specify the following settings:
You set EvaluateTargetHealth to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).
You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.
You specify a health check ID for the non-alias resource record set.



If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.
If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.

Note

The alias resource record set can also route traffic to a group of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.

Geolocation Routing

For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has * for CountryCode is * , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:

The United States
North America
The default resource record set


Specifying the Health Check Endpoint by Domain Name

If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com . For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com ), not the name of the resource record sets (www.example.com ).

Warning
Health check results will be unpredictable if you do the following:

Create a health check that has the same value for FullyQualifiedDomainName as the name of a resource record set.
Associate that health check with the resource record set.



TrafficPolicyInstanceId (string) --
When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. TrafficPolicyInstanceId is the ID of the traffic policy instance that Route 53 created this resource record set for.

Warning
To delete the resource record set that is associated with a traffic policy instance, use DeleteTrafficPolicyInstance . Route 53 will delete the resource record set automatically. If you delete the resource record set by using ChangeResourceRecordSets , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use.






IsTruncated (boolean) --
A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the NextRecordName element.

NextRecordName (string) --
If the results were truncated, the name of the next record in the list.
This element is present only if IsTruncated is true.

NextRecordType (string) --
If the results were truncated, the type of the next record in the list.
This element is present only if IsTruncated is true.

NextRecordIdentifier (string) --

Resource record sets that have a routing policy other than simple: If results were truncated for a given DNS name and type, the value of SetIdentifier for the next resource record set that has the current DNS name and type.

For information about routing policies, see Choosing a Routing Policy in the Amazon Route 53 Developer Guide .

MaxItems (string) --
The maximum number of records you requested.







Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput


    :return: {
        'ResourceRecordSets': [
            {
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'SetIdentifier': 'string',
                'Weight': 123,
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-north-1'|'cn-northwest-1'|'ap-east-1'|'me-south-1'|'ap-south-1'|'af-south-1'|'eu-south-1',
                'GeoLocation': {
                    'ContinentCode': 'string',
                    'CountryCode': 'string',
                    'SubdivisionCode': 'string'
                },
                'Failover': 'PRIMARY'|'SECONDARY',
                'MultiValueAnswer': True|False,
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
        'NextRecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'NextRecordIdentifier': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    The * must replace the entire label. For example, you can\'t specify *prod.example.com or prod*.example.com .
    The * can\'t replace any of the middle labels, for example, marketing.*.example.com.
    If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.
    
    """
    pass

def list_reusable_delegation_sets(Marker=None, MaxItems=None):
    """
    Retrieves a list of the reusable delegation sets that are associated with the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_reusable_delegation_sets(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: If the value of IsTruncated in the previous response was true , you have more reusable delegation sets. To get another group, submit another ListReusableDelegationSets request.\nFor the value of marker , specify the value of NextMarker from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more reusable delegation sets to get.\n

    :type MaxItems: string
    :param MaxItems: The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
A complex type that contains information about the reusable delegation sets that are associated with the current AWS account.

DelegationSets (list) --
A complex type that contains one DelegationSet element for each reusable delegation set that was created by the current AWS account.

(dict) --
A complex type that lists the name servers in a delegation set, as well as the CallerReference and the ID for the delegation set.

Id (string) --
The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference (string) --
The value that you specified for CallerReference when you created the reusable delegation set.

NameServers (list) --
A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string) --






Marker (string) --
For the second and subsequent calls to ListReusableDelegationSets , Marker is the value that you specified for the marker parameter in the request that produced the current response.

IsTruncated (boolean) --
A flag that indicates whether there are more reusable delegation sets to be listed.

NextMarker (string) --
If IsTruncated is true , the value of NextMarker identifies the next reusable delegation set that Amazon Route 53 will return if you submit another ListReusableDelegationSets request and specify the value of NextMarker in the marker parameter.

MaxItems (string) --
The value that you specified for the maxitems parameter in the call to ListReusableDelegationSets that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput


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
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceType='healthcheck'|'hostedzone',
        ResourceId='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of the resource.\n\nThe resource type for health checks is healthcheck .\nThe resource type for hosted zones is hostedzone .\n\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource for which you want to retrieve tags.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
A complex type that contains information about the health checks or hosted zones for which you want to list tags.

ResourceTagSet (dict) --
A ResourceTagSet containing tags associated with the specified resource.

ResourceType (string) --
The type of the resource.

The resource type for health checks is healthcheck .
The resource type for hosted zones is hostedzone .


ResourceId (string) --
The ID for the specified resource.

Tags (list) --
The tags associated with the specified resource.

(dict) --
A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

Key (string) --
The value of Key depends on the operation that you want to perform:

Add a tag to a health check or hosted zone : Key is the name that you want to give the new tag.
Edit a tag : Key is the name of the tag that you want to change the Value for.
Delete a key : Key is the name of the tag you want to remove.
Give a name to a health check : Edit the default Name tag. In the Amazon Route 53 console, the list of your health checks includes a Name column that lets you see the name that you\'ve given to each health check.


Value (string) --
The value of Value depends on the operation that you want to perform:

Add a tag to a health check or hosted zone : Value is the value that you want to give the new tag.
Edit a tag : Value is the new value that you want to assign the tag.














Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.PriorRequestNotComplete
Route53.Client.exceptions.ThrottlingException


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
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resources(
        ResourceType='healthcheck'|'hostedzone',
        ResourceIds=[
            'string',
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of the resources.\n\nThe resource type for health checks is healthcheck .\nThe resource type for hosted zones is hostedzone .\n\n

    :type ResourceIds: list
    :param ResourceIds: [REQUIRED]\nA complex type that contains the ResourceId element for each resource for which you want to get a list of tags.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
A complex type containing tags for the specified resources.

ResourceTagSets (list) --
A list of ResourceTagSet s containing tags associated with the specified resources.

(dict) --
A complex type containing a resource and its associated tags.

ResourceType (string) --
The type of the resource.

The resource type for health checks is healthcheck .
The resource type for hosted zones is hostedzone .


ResourceId (string) --
The ID for the specified resource.

Tags (list) --
The tags associated with the specified resource.

(dict) --
A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

Key (string) --
The value of Key depends on the operation that you want to perform:

Add a tag to a health check or hosted zone : Key is the name that you want to give the new tag.
Edit a tag : Key is the name of the tag that you want to change the Value for.
Delete a key : Key is the name of the tag you want to remove.
Give a name to a health check : Edit the default Name tag. In the Amazon Route 53 console, the list of your health checks includes a Name column that lets you see the name that you\'ve given to each health check.


Value (string) --
The value of Value depends on the operation that you want to perform:

Add a tag to a health check or hosted zone : Value is the value that you want to give the new tag.
Edit a tag : Value is the new value that you want to assign the tag.
















Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.PriorRequestNotComplete
Route53.Client.exceptions.ThrottlingException


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
    Gets information about the latest version for every traffic policy that is associated with the current AWS account. Policies are listed in the order that they were created in.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_traffic_policies(
        TrafficPolicyIdMarker='string',
        MaxItems='string'
    )
    
    
    :type TrafficPolicyIdMarker: string
    :param TrafficPolicyIdMarker: (Conditional) For your first request to ListTrafficPolicies , don\'t include the TrafficPolicyIdMarker parameter.\nIf you have more traffic policies than the value of MaxItems , ListTrafficPolicies returns only the first MaxItems traffic policies. To get the next group of policies, submit another request to ListTrafficPolicies . For the value of TrafficPolicyIdMarker , specify the value of TrafficPolicyIdMarker that was returned in the previous response.\n

    :type MaxItems: string
    :param MaxItems: (Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than MaxItems traffic policies, the value of IsTruncated in the response is true , and the value of TrafficPolicyIdMarker is the ID of the first traffic policy that Route 53 will return if you submit another request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicySummaries': [
        {
            'Id': 'string',
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'LatestVersion': 123,
            'TrafficPolicyCount': 123
        },
    ],
    'IsTruncated': True|False,
    'TrafficPolicyIdMarker': 'string',
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicySummaries (list) --
A list that contains one TrafficPolicySummary element for each traffic policy that was created by the current AWS account.

(dict) --
A complex type that contains information about the latest version of one traffic policy that is associated with the current AWS account.

Id (string) --
The ID that Amazon Route 53 assigned to the traffic policy when you created it.

Name (string) --
The name that you specified for the traffic policy when you created it.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

LatestVersion (integer) --
The version number of the latest version of the traffic policy.

TrafficPolicyCount (integer) --
The number of traffic policies that are associated with the current AWS account.





IsTruncated (boolean) --
A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another ListTrafficPolicies request and specifying the value of TrafficPolicyIdMarker in the TrafficPolicyIdMarker request parameter.

TrafficPolicyIdMarker (string) --
If the value of IsTruncated is true , TrafficPolicyIdMarker is the ID of the first traffic policy in the next group of MaxItems traffic policies.

MaxItems (string) --
The value that you specified for the MaxItems parameter in the ListTrafficPolicies request that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput


    :return: {
        'TrafficPolicySummaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'LatestVersion': 123,
                'TrafficPolicyCount': 123
            },
        ],
        'IsTruncated': True|False,
        'TrafficPolicyIdMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def list_traffic_policy_instances(HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created by using the current AWS account.
    Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_traffic_policy_instances(
        HostedZoneIdMarker='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        MaxItems='string'
    )
    
    
    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of HostedZoneId , specify the value of HostedZoneIdMarker from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of trafficpolicyinstancename , specify the value of TrafficPolicyInstanceNameMarker from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of trafficpolicyinstancetype , specify the value of TrafficPolicyInstanceTypeMarker from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a ListTrafficPolicyInstances request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance in the next group of MaxItems traffic policy instances.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
        },
    ],
    'HostedZoneIdMarker': 'string',
    'TrafficPolicyInstanceNameMarker': 'string',
    'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
    'IsTruncated': True|False,
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicyInstances (list) --
A list that contains one TrafficPolicyInstance element for each traffic policy instance that matches the elements in the request.

(dict) --
A complex type that contains settings for the new traffic policy instance.

Id (string) --
The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId (string) --
The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name (string) --
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL (integer) --
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State (string) --
The value of State is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed

Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --
If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.





HostedZoneIdMarker (string) --
If IsTruncated is true , HostedZoneIdMarker is the ID of the hosted zone of the first traffic policy instance that Route 53 will return if you submit another ListTrafficPolicyInstances request.

TrafficPolicyInstanceNameMarker (string) --
If IsTruncated is true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance that Route 53 will return if you submit another ListTrafficPolicyInstances request.

TrafficPolicyInstanceTypeMarker (string) --
If IsTruncated is true , TrafficPolicyInstanceTypeMarker is the DNS type of the resource record sets that are associated with the first traffic policy instance that Amazon Route 53 will return if you submit another ListTrafficPolicyInstances request.

IsTruncated (boolean) --
A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get more traffic policy instances by calling ListTrafficPolicyInstances again and specifying the values of the HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker in the corresponding request parameters.

MaxItems (string) --
The value that you specified for the MaxItems parameter in the call to ListTrafficPolicyInstances that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicyInstance


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
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            },
        ],
        'HostedZoneIdMarker': 'string',
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchTrafficPolicyInstance
    
    """
    pass

def list_traffic_policy_instances_by_hosted_zone(HostedZoneId=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created in a specified hosted zone.
    Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_traffic_policy_instances_by_hosted_zone(
        HostedZoneId='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        MaxItems='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that you want to list traffic policy instances for.\n

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: If the value of IsTruncated in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of trafficpolicyinstancename , specify the value of TrafficPolicyInstanceNameMarker from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: If the value of IsTruncated in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstances request. For the value of trafficpolicyinstancetype , specify the value of TrafficPolicyInstanceTypeMarker from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
        },
    ],
    'TrafficPolicyInstanceNameMarker': 'string',
    'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
    'IsTruncated': True|False,
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicyInstances (list) --
A list that contains one TrafficPolicyInstance element for each traffic policy instance that matches the elements in the request.

(dict) --
A complex type that contains settings for the new traffic policy instance.

Id (string) --
The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId (string) --
The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name (string) --
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL (integer) --
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State (string) --
The value of State is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed

Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --
If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.





TrafficPolicyInstanceNameMarker (string) --
If IsTruncated is true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of traffic policy instances.

TrafficPolicyInstanceTypeMarker (string) --
If IsTruncated is true, TrafficPolicyInstanceTypeMarker is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of traffic policy instances.

IsTruncated (boolean) --
A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by submitting another ListTrafficPolicyInstancesByHostedZone request and specifying the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker in the corresponding request parameters.

MaxItems (string) --
The value that you specified for the MaxItems parameter in the ListTrafficPolicyInstancesByHostedZone request that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicyInstance
Route53.Client.exceptions.NoSuchHostedZone


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
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            },
        ],
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchTrafficPolicyInstance
    Route53.Client.exceptions.NoSuchHostedZone
    
    """
    pass

def list_traffic_policy_instances_by_policy(TrafficPolicyId=None, TrafficPolicyVersion=None, HostedZoneIdMarker=None, TrafficPolicyInstanceNameMarker=None, TrafficPolicyInstanceTypeMarker=None, MaxItems=None):
    """
    Gets information about the traffic policy instances that you created by using a specify traffic policy version.
    Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the MaxItems parameter to list them in groups of up to 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_traffic_policy_instances_by_policy(
        TrafficPolicyId='string',
        TrafficPolicyVersion=123,
        HostedZoneIdMarker='string',
        TrafficPolicyInstanceNameMarker='string',
        TrafficPolicyInstanceTypeMarker='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        MaxItems='string'
    )
    
    
    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]\nThe ID of the traffic policy for which you want to list traffic policy instances.\n

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]\nThe version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by TrafficPolicyId .\n

    :type HostedZoneIdMarker: string
    :param HostedZoneIdMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstancesByPolicy request.\nFor the value of hostedzoneid , specify the value of HostedZoneIdMarker from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type TrafficPolicyInstanceNameMarker: string
    :param TrafficPolicyInstanceNameMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstancesByPolicy request.\nFor the value of trafficpolicyinstancename , specify the value of TrafficPolicyInstanceNameMarker from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type TrafficPolicyInstanceTypeMarker: string
    :param TrafficPolicyInstanceTypeMarker: If the value of IsTruncated in the previous response was true , you have more traffic policy instances. To get more traffic policy instances, submit another ListTrafficPolicyInstancesByPolicy request.\nFor the value of trafficpolicyinstancetype , specify the value of TrafficPolicyInstanceTypeMarker from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.\nIf the value of IsTruncated in the previous response was false , there are no more traffic policy instances to get.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than MaxItems traffic policy instances, the value of the IsTruncated element in the response is true , and the values of HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
        },
    ],
    'HostedZoneIdMarker': 'string',
    'TrafficPolicyInstanceNameMarker': 'string',
    'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
    'IsTruncated': True|False,
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicyInstances (list) --
A list that contains one TrafficPolicyInstance element for each traffic policy instance that matches the elements in the request.

(dict) --
A complex type that contains settings for the new traffic policy instance.

Id (string) --
The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId (string) --
The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name (string) --
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL (integer) --
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State (string) --
The value of State is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed

Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --
If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.





HostedZoneIdMarker (string) --
If IsTruncated is true , HostedZoneIdMarker is the ID of the hosted zone of the first traffic policy instance in the next group of traffic policy instances.

TrafficPolicyInstanceNameMarker (string) --
If IsTruncated is true , TrafficPolicyInstanceNameMarker is the name of the first traffic policy instance in the next group of MaxItems traffic policy instances.

TrafficPolicyInstanceTypeMarker (string) --
If IsTruncated is true , TrafficPolicyInstanceTypeMarker is the DNS type of the resource record sets that are associated with the first traffic policy instance in the next group of MaxItems traffic policy instances.

IsTruncated (boolean) --
A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get the next group of traffic policy instances by calling ListTrafficPolicyInstancesByPolicy again and specifying the values of the HostedZoneIdMarker , TrafficPolicyInstanceNameMarker , and TrafficPolicyInstanceTypeMarker elements in the corresponding request parameters.

MaxItems (string) --
The value that you specified for the MaxItems parameter in the call to ListTrafficPolicyInstancesByPolicy that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicyInstance
Route53.Client.exceptions.NoSuchTrafficPolicy


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
                'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
            },
        ],
        'HostedZoneIdMarker': 'string',
        'TrafficPolicyInstanceNameMarker': 'string',
        'TrafficPolicyInstanceTypeMarker': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'IsTruncated': True|False,
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchTrafficPolicyInstance
    Route53.Client.exceptions.NoSuchTrafficPolicy
    
    """
    pass

def list_traffic_policy_versions(Id=None, TrafficPolicyVersionMarker=None, MaxItems=None):
    """
    Gets information about all of the versions for a specified traffic policy.
    Traffic policy versions are listed in numerical order by VersionNumber .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_traffic_policy_versions(
        Id='string',
        TrafficPolicyVersionMarker='string',
        MaxItems='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nSpecify the value of Id of the traffic policy for which you want to list all versions.\n

    :type TrafficPolicyVersionMarker: string
    :param TrafficPolicyVersionMarker: For your first request to ListTrafficPolicyVersions , don\'t include the TrafficPolicyVersionMarker parameter.\nIf you have more traffic policy versions than the value of MaxItems , ListTrafficPolicyVersions returns only the first group of MaxItems versions. To get more traffic policy versions, submit another ListTrafficPolicyVersions request. For the value of TrafficPolicyVersionMarker , specify the value of TrafficPolicyVersionMarker in the previous response.\n

    :type MaxItems: string
    :param MaxItems: The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than MaxItems versions, the value of IsTruncated in the response is true , and the value of the TrafficPolicyVersionMarker element is the ID of the first version that Route 53 will return if you submit another request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicies': [
        {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'Document': 'string',
            'Comment': 'string'
        },
    ],
    'IsTruncated': True|False,
    'TrafficPolicyVersionMarker': 'string',
    'MaxItems': 'string'
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

TrafficPolicies (list) --
A list that contains one TrafficPolicy element for each traffic policy version that is associated with the specified traffic policy.

(dict) --
A complex type that contains settings for a traffic policy.

Id (string) --
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

Version (integer) --
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of Version is always 1.

Name (string) --
The name that you specified when you created the traffic policy.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

Document (string) --
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the CreateTrafficPolicy request. For more information about the JSON format, see Traffic Policy Document Format .

Comment (string) --
The comment that you specify in the CreateTrafficPolicy request, if any.





IsTruncated (boolean) --
A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another ListTrafficPolicyVersions request and specifying the value of NextMarker in the marker parameter.

TrafficPolicyVersionMarker (string) --
If IsTruncated is true , the value of TrafficPolicyVersionMarker identifies the first traffic policy that Amazon Route 53 will return if you submit another request. Call ListTrafficPolicyVersions again and specify the value of TrafficPolicyVersionMarker in the TrafficPolicyVersionMarker request parameter.
This element is present only if IsTruncated is true .

MaxItems (string) --
The value that you specified for the maxitems parameter in the ListTrafficPolicyVersions request that produced the current response.







Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicy


    :return: {
        'TrafficPolicies': [
            {
                'Id': 'string',
                'Version': 123,
                'Name': 'string',
                'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
                'Document': 'string',
                'Comment': 'string'
            },
        ],
        'IsTruncated': True|False,
        'TrafficPolicyVersionMarker': 'string',
        'MaxItems': 'string'
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchTrafficPolicy
    
    """
    pass

def list_vpc_association_authorizations(HostedZoneId=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you\'ve submitted one or more CreateVPCAssociationAuthorization requests.
    The response includes a VPCs element with a VPC child element for each VPC that can be associated with the hosted zone.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_vpc_association_authorizations(
        HostedZoneId='string',
        NextToken='string',
        MaxResults='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.\n

    :type NextToken: string
    :param NextToken: Optional : If a response includes a NextToken element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of NextToken from the response in the nexttoken parameter in another ListVPCAssociationAuthorizations request.

    :type MaxResults: string
    :param MaxResults: Optional : An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don\'t specify a value for MaxResults , Route 53 returns up to 50 VPCs per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZoneId': 'string',
    'NextToken': 'string',
    'VPCs': [
        {
            'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
            'VPCId': 'string'
        },
    ]
}


Response Structure

(dict) --
A complex type that contains the response information for the request.

HostedZoneId (string) --
The ID of the hosted zone that you can associate the listed VPCs with.

NextToken (string) --
When the response includes a NextToken element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of VPCs, submit another ListVPCAssociationAuthorizations request, and include the value of the NextToken element from the response in the nexttoken request parameter.

VPCs (list) --
The list of VPCs that are authorized to be associated with the specified hosted zone.

(dict) --
(Private hosted zones only) A complex type that contains information about an Amazon VPC.

VPCRegion (string) --
(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId (string) --
(Private hosted zones only) The ID of an Amazon VPC.











Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.InvalidPaginationToken


    :return: {
        'HostedZoneId': 'string',
        'NextToken': 'string',
        'VPCs': [
            {
                'VPCRegion': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ap-east-1'|'me-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-south-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'ca-central-1'|'cn-north-1'|'af-south-1'|'eu-south-1',
                'VPCId': 'string'
            },
        ]
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.InvalidPaginationToken
    
    """
    pass

def test_dns_answer(HostedZoneId=None, RecordName=None, RecordType=None, ResolverIP=None, EDNS0ClientSubnetIP=None, EDNS0ClientSubnetMask=None):
    """
    Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_dns_answer(
        HostedZoneId='string',
        RecordName='string',
        RecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        ResolverIP='string',
        EDNS0ClientSubnetIP='string',
        EDNS0ClientSubnetMask='string'
    )
    
    
    :type HostedZoneId: string
    :param HostedZoneId: [REQUIRED]\nThe ID of the hosted zone that you want Amazon Route 53 to simulate a query for.\n

    :type RecordName: string
    :param RecordName: [REQUIRED]\nThe name of the resource record set that you want Amazon Route 53 to simulate a query for.\n

    :type RecordType: string
    :param RecordType: [REQUIRED]\nThe type of the resource record set.\n

    :type ResolverIP: string
    :param ResolverIP: If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, TestDnsAnswer uses the IP address of a DNS resolver in the AWS US East (N. Virginia) Region (us-east-1 ).

    :type EDNS0ClientSubnetIP: string
    :param EDNS0ClientSubnetIP: If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, 192.0.2.44 or 2001:db8:85a3::8a2e:370:7334 .

    :type EDNS0ClientSubnetMask: string
    :param EDNS0ClientSubnetMask: If you specify an IP address for edns0clientsubnetip , you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify 192.0.2.44 for edns0clientsubnetip and 24 for edns0clientsubnetmask , the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.\nThe range of valid values depends on whether edns0clientsubnetip is an IPv4 or an IPv6 address:\n\nIPv4 : Specify a value between 0 and 32\nIPv6 : Specify a value between 0 and 128\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Nameserver': 'string',
    'RecordName': 'string',
    'RecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
    'RecordData': [
        'string',
    ],
    'ResponseCode': 'string',
    'Protocol': 'string'
}


Response Structure

(dict) --
A complex type that contains the response to a TestDNSAnswer request.

Nameserver (string) --
The Amazon Route 53 name server used to respond to the request.

RecordName (string) --
The name of the resource record set that you submitted a request for.

RecordType (string) --
The type of the resource record set that you submitted a request for.

RecordData (list) --
A list that contains values that Amazon Route 53 returned for this resource record set.

(string) --
A value that Amazon Route 53 returned for this resource record set. A RecordDataEntry element is one of the following:

For non-alias resource record sets, a RecordDataEntry element contains one value in the resource record set. If the resource record set contains multiple values, the response includes one RecordDataEntry element for each value.
For multiple resource record sets that have the same name and type, which includes weighted, latency, geolocation, and failover, a RecordDataEntry element contains the value from the appropriate resource record set based on the request.
For alias resource record sets that refer to AWS resources other than another resource record set, the RecordDataEntry element contains an IP address or a domain name for the AWS resource, depending on the type of resource.
For alias resource record sets that refer to other resource record sets, a RecordDataEntry element contains one value from the referenced resource record set. If the referenced resource record set contains multiple values, the response includes one RecordDataEntry element for each value.




ResponseCode (string) --
A code that indicates whether the request is valid or not. The most common response code is NOERROR , meaning that the request is valid. If the response is not valid, Amazon Route 53 returns a response code that describes the error. For a list of possible response codes, see DNS RCODES on the IANA website.

Protocol (string) --
The protocol that Amazon Route 53 used to respond to the request, either UDP or TCP .







Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput


    :return: {
        'Nameserver': 'string',
        'RecordName': 'string',
        'RecordType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
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

def update_health_check(HealthCheckId=None, HealthCheckVersion=None, IPAddress=None, Port=None, ResourcePath=None, FullyQualifiedDomainName=None, SearchString=None, FailureThreshold=None, Inverted=None, Disabled=None, HealthThreshold=None, ChildHealthChecks=None, EnableSNI=None, Regions=None, AlarmIdentifier=None, InsufficientDataHealthStatus=None, ResetElements=None):
    """
    Updates an existing health check. Note that some values can\'t be updated.
    For more information about updating health checks, see Creating, Updating, and Deleting Health Checks in the Amazon Route 53 Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
        Disabled=True|False,
        HealthThreshold=123,
        ChildHealthChecks=[
            'string',
        ],
        EnableSNI=True|False,
        Regions=[
            'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
        ],
        AlarmIdentifier={
            'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
            'Name': 'string'
        },
        InsufficientDataHealthStatus='Healthy'|'Unhealthy'|'LastKnownStatus',
        ResetElements=[
            'FullyQualifiedDomainName'|'Regions'|'ResourcePath'|'ChildHealthChecks',
        ]
    )
    
    
    :type HealthCheckId: string
    :param HealthCheckId: [REQUIRED]\nThe ID for the health check for which you want detailed information. When you created the health check, CreateHealthCheck returned the ID in the response, in the HealthCheckId element.\n

    :type HealthCheckVersion: integer
    :param HealthCheckVersion: A sequential counter that Amazon Route 53 sets to 1 when you create a health check and increments by 1 each time you update settings for the health check.\nWe recommend that you use GetHealthCheck or ListHealthChecks to get the current value of HealthCheckVersion for the health check that you want to update, and that you include that value in your UpdateHealthCheck request. This prevents Route 53 from overwriting an intervening update:\n\nIf the value in the UpdateHealthCheck request matches the value of HealthCheckVersion in the health check, Route 53 updates the health check with the new settings.\nIf the value of HealthCheckVersion in the health check is greater, the health check was changed after you got the version number. Route 53 does not update the health check, and it returns a HealthCheckVersionMismatch error.\n\n

    :type IPAddress: string
    :param IPAddress: The IPv4 or IPv6 IP address for the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address that is returned by DNS, Route 53 then checks the health of the endpoint.\nUse one of the following formats for the value of IPAddress :\n\nIPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .\nIPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .\n\nIf the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance never changes. For more information, see the applicable documentation:\n\nLinux: Elastic IP Addresses (EIP) in the Amazon EC2 User Guide for Linux Instances\nWindows: Elastic IP Addresses (EIP) in the Amazon EC2 User Guide for Windows Instances\n\n\nNote\nIf a health check already has a value for IPAddress , you can change the value. However, you can\'t update an existing health check to add or remove the value of IPAddress .\n\nFor more information, see FullyQualifiedDomainName .\nConstraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:\n\nRFC 5735, Special Use IPv4 Addresses\nRFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space\nRFC 5156, Special-Use IPv6 Addresses\n\n

    :type Port: integer
    :param Port: The port on the endpoint that you want Amazon Route 53 to perform health checks on.\n\nNote\nDon\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .\n\n

    :type ResourcePath: string
    :param ResourcePath: The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .\nSpecify this value only if you want to change it.\n

    :type FullyQualifiedDomainName: string
    :param FullyQualifiedDomainName: Amazon Route 53 behavior depends on whether you specify a value for IPAddress .\n\nNote\n\nIf a health check already has a value for IPAddress , you can change the value. However, you can\'t update an existing health check to add or remove the value of IPAddress .\nIf you specify a value for IPAddress :\n\nRoute 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.\nWhen Route 53 checks the health of an endpoint, here is how it constructs the Host header:\n\nIf you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.\nIf you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.\nIf you specify another value for Port and any value except TCP for Type , Route 53 passes * FullyQualifiedDomainName :Port * to the endpoint in the Host header.\n\nIf you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the above cases.\n\nIf you don\'t specify a value for IPAddress :\nIf you don\'t specify a value for IPAddress , Route 53 sends a DNS request to the domain that you specify in FullyQualifiedDomainName at the interval you specify in RequestInterval . Using an IPv4 address that is returned by DNS, Route 53 then checks the health of the endpoint.\n\nNote\nIf you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a 'DNS resolution failed' error.\n\nIf you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com ), not the name of the resource record sets (www.example.com).\n\nWarning\nIn this configuration, if the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.\n\nIn addition, if the value of Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.\n

    :type SearchString: string
    :param SearchString: If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy. (You can\'t change the value of Type when you update a health check.)

    :type FailureThreshold: integer
    :param FailureThreshold: The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .\nIf you don\'t specify a value for FailureThreshold , the default value is three health checks.\n

    :type Inverted: boolean
    :param Inverted: Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

    :type Disabled: boolean
    :param Disabled: Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:\n\nHealth checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.\nCalculated health checks: Route 53 stops aggregating the status of the referenced health checks.\nHealth checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.\n\nAfter you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .\nCharges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .\n

    :type HealthThreshold: integer
    :param HealthThreshold: The number of child health checks that are associated with a CALCULATED health that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks and ChildHealthCheck elements.\nNote the following:\n\nIf you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.\nIf you specify 0 , Route 53 always considers this health check to be healthy.\n\n

    :type ChildHealthChecks: list
    :param ChildHealthChecks: A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.\n\n(string) --\n\n

    :type EnableSNI: boolean
    :param EnableSNI: Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.\nSome endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.\nThe SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.\n

    :type Regions: list
    :param Regions: A complex type that contains one Region element for each region that you want Amazon Route 53 health checkers to check the specified endpoint from.\n\n(string) --\n\n

    :type AlarmIdentifier: dict
    :param AlarmIdentifier: A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.\n\nRegion (string) -- [REQUIRED]For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.\nFor the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .\n\nName (string) -- [REQUIRED]The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.\n\nNote\nRoute 53 supports CloudWatch alarms with the following features:\n\nStandard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .\nStatistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.\n\n\n\n\n

    :type InsufficientDataHealthStatus: string
    :param InsufficientDataHealthStatus: When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:\n\nHealthy : Route 53 considers the health check to be healthy.\nUnhealthy : Route 53 considers the health check to be unhealthy.\nLastKnownStatus : Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.\n\n

    :type ResetElements: list
    :param ResetElements: A complex type that contains one ResettableElementName element for each element that you want to reset to the default value. Valid values for ResettableElementName include the following:\n\nChildHealthChecks : Amazon Route 53 resets ChildHealthChecks to null.\nFullyQualifiedDomainName : Route 53 resets FullyQualifiedDomainName . to null.\nRegions : Route 53 resets the Regions list to the default set of regions.\nResourcePath : Route 53 resets ResourcePath to null.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HealthCheck': {
        'Id': 'string',
        'CallerReference': 'string',
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        },
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
            'Disabled': True|False,
            'HealthThreshold': 123,
            'ChildHealthChecks': [
                'string',
            ],
            'EnableSNI': True|False,
            'Regions': [
                'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
            ],
            'AlarmIdentifier': {
                'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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

(dict) --
A complex type that contains the response to the UpdateHealthCheck request.

HealthCheck (dict) --
A complex type that contains the response to an UpdateHealthCheck request.

Id (string) --
The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

CallerReference (string) --
A unique string that you specified when you created the health check.

LinkedService (dict) --
If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can\'t edit or delete it using Amazon Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.



HealthCheckConfig (dict) --
A complex type that contains detailed information about one health check.

IPAddress (string) --
The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for IPAddress , Route 53 sends a DNS request to resolve the domain name that you specify in FullyQualifiedDomainName at the interval that you specify in RequestInterval . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
Use one of the following formats for the value of IPAddress :

IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .

If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for IPAddress . This ensures that the IP address of your instance will never change.
For more information, see FullyQualifiedDomainName .
Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:

RFC 5735, Special Use IPv4 Addresses
RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
RFC 5156, Special-Use IPv6 Addresses

When the value of Type is CALCULATED or CLOUDWATCH_METRIC , omit IPAddress .

Port (integer) --
The port on the endpoint that you want Amazon Route 53 to perform health checks on.

Note
Don\'t specify a value for Port when you specify a value for Type of CLOUDWATCH_METRIC or CALCULATED .


Type (string) --
The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

Warning
You can\'t change the value of Type after you create a health check.

You can create the following types of health checks:

HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.


Warning
If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.


HTTP_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
HTTPS_STR_MATCH : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and searches the first 5,120 bytes of the response body for the string that you specify in SearchString .
TCP : Route 53 tries to establish a TCP connection.
CLOUDWATCH_METRIC : The health check is associated with a CloudWatch alarm. If the state of the alarm is OK , the health check is considered healthy. If the state is ALARM , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is OK or ALARM , the health check status depends on the setting for InsufficientDataHealthStatus : Healthy , Unhealthy , or LastKnownStatus .
CALCULATED : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of HealthThreshold .

For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .

ResourcePath (string) --
The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, /welcome.html?language=jp&login=y .

FullyQualifiedDomainName (string) --
Amazon Route 53 behavior depends on whether you specify a value for IPAddress .

If you specify a value for IPAddress :

Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of FullyQualifiedDomainName in the Host header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
When Route 53 checks the health of an endpoint, here is how it constructs the Host header:

If you specify a value of 80 for Port and HTTP or HTTP_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify a value of 443 for Port and HTTPS or HTTPS_STR_MATCH for Type , Route 53 passes the value of FullyQualifiedDomainName to the endpoint in the Host header.
If you specify another value for Port and any value except TCP for Type , Route 53 passes FullyQualifiedDomainName:Port to the endpoint in the Host header.

If you don\'t specify a value for FullyQualifiedDomainName , Route 53 substitutes the value of IPAddress in the Host header in each of the preceding cases.

**If you don\'t specify a value for IPAddress ** :

Route 53 sends a DNS request to the domain that you specify for FullyQualifiedDomainName at the interval that you specify for RequestInterval . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

Note
If you don\'t specify a value for IPAddress , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for FullyQualifiedDomainName , the health check fails with a "DNS resolution failed" error.

If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by FullyQualifiedDomainName , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of FullyQualifiedDomainName , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

Warning
In this configuration, if you create a health check for which the value of FullyQualifiedDomainName matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

In addition, if the value that you specify for Type is HTTP , HTTPS , HTTP_STR_MATCH , or HTTPS_STR_MATCH , Route 53 passes the value of FullyQualifiedDomainName in the Host header, as it does when you specify a value for IPAddress . If the value of Type is TCP , Route 53 doesn\'t pass a Host header.

SearchString (string) --
If the value of Type is HTTP_STR_MATCH or HTTPS_STR_MATCH , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
Route 53 considers case when searching for SearchString in the response body.

RequestInterval (integer) --
The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.

Warning
You can\'t change the value of RequestInterval after you create a health check.

If you don\'t specify a value for RequestInterval , the default value is 30 seconds.

FailureThreshold (integer) --
The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Amazon Route 53 Determines Whether an Endpoint Is Healthy in the Amazon Route 53 Developer Guide .
If you don\'t specify a value for FailureThreshold , the default value is three health checks.

MeasureLatency (boolean) --
Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the Health Checks page in the Route 53 console.

Warning
You can\'t change the value of MeasureLatency after you create a health check.


Inverted (boolean) --
Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

Disabled (boolean) --
Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:

Health checks that check the health of endpoints: Route 53 stops submitting requests to your application, server, or other resource.
Calculated health checks: Route 53 stops aggregating the status of the referenced health checks.
Health checks that monitor CloudWatch alarms: Route 53 stops monitoring the corresponding CloudWatch metrics.

After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of Inverted .
Charges for a health check still apply when the health check is disabled. For more information, see Amazon Route 53 Pricing .

HealthThreshold (integer) --
The number of child health checks that are associated with a CALCULATED health check that Amazon Route 53 must consider healthy for the CALCULATED health check to be considered healthy. To specify the child health checks that you want to associate with a CALCULATED health check, use the ChildHealthChecks element.
Note the following:

If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
If you specify 0 , Route 53 always considers this health check to be healthy.


ChildHealthChecks (list) --
(CALCULATED Health Checks Only) A complex type that contains one ChildHealthCheck element for each health check that you want to associate with a CALCULATED health check.

(string) --


EnableSNI (boolean) --
Specify whether you want Amazon Route 53 to send the value of FullyQualifiedDomainName to the endpoint in the client_hello message during TLS negotiation. This allows the endpoint to respond to HTTPS health check requests with the applicable SSL/TLS certificate.
Some endpoints require that HTTPS requests include the host name in the client_hello message. If you don\'t enable SNI, the status of the health check will be SSL alert handshake_failure . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
The SSL/TLS certificate on your endpoint includes a domain name in the Common Name field and possibly several more in the Subject Alternative Names field. One of the domain names in the certificate should match the value that you specify for FullyQualifiedDomainName . If the endpoint responds to the client_hello message with a certificate that does not include the domain name that you specified in FullyQualifiedDomainName , a health checker will retry the handshake. In the second attempt, the health checker will omit FullyQualifiedDomainName from the client_hello message.

Regions (list) --
A complex type that contains one Region element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under Valid Values .
If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

(string) --


AlarmIdentifier (dict) --
A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

Region (string) --
For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
For the current list of CloudWatch regions, see Amazon CloudWatch in the AWS Service Endpoints chapter of the Amazon Web Services General Reference .

Name (string) --
The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

Note
Route 53 supports CloudWatch alarms with the following features:

Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported.





InsufficientDataHealthStatus (string) --
When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

Healthy : Route 53 considers the health check to be healthy.
Unhealthy : Route 53 considers the health check to be unhealthy.
LastKnownStatus : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.




HealthCheckVersion (integer) --
The version of the health check. You can optionally pass this value in a call to UpdateHealthCheck to prevent overwriting another change to the health check.

CloudWatchAlarmConfiguration (dict) --
A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

EvaluationPeriods (integer) --
For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

Threshold (float) --
For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

ComparisonOperator (string) --
For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

Period (integer) --
For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

MetricName (string) --
The name of the CloudWatch metric that the alarm is associated with.

Namespace (string) --
The namespace of the metric that the alarm is associated with. For more information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

Statistic (string) --
For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

Dimensions (list) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference in the Amazon CloudWatch User Guide .

(dict) --
For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

Name (string) --
For the metric that the CloudWatch alarm is associated with, the name of one dimension.

Value (string) --
For the metric that the CloudWatch alarm is associated with, the value of one dimension.















Exceptions

Route53.Client.exceptions.NoSuchHealthCheck
Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.HealthCheckVersionMismatch


    :return: {
        'HealthCheck': {
            'Id': 'string',
            'CallerReference': 'string',
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            },
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
                'Disabled': True|False,
                'HealthThreshold': 123,
                'ChildHealthChecks': [
                    'string',
                ],
                'EnableSNI': True|False,
                'Regions': [
                    'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1',
                ],
                'AlarmIdentifier': {
                    'Region': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'ap-east-1'|'me-south-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'eu-north-1'|'sa-east-1'|'cn-northwest-1'|'cn-north-1'|'af-south-1'|'eu-south-1'|'us-gov-west-1'|'us-gov-east-1'|'us-iso-east-1'|'us-isob-east-1',
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
    IPv4 address : four values between 0 and 255, separated by periods (.), for example, 192.0.2.44 .
    IPv6 address : eight groups of four hexadecimal values, separated by colons (:), for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 . You can also shorten IPv6 addresses as described in RFC 5952, for example, 2001:db8:85a3::abcd:1:2345 .
    
    """
    pass

def update_hosted_zone_comment(Id=None, Comment=None):
    """
    Updates the comment for a specified hosted zone.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_hosted_zone_comment(
        Id='string',
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID for the hosted zone that you want to update the comment for.\n

    :type Comment: string
    :param Comment: The new comment for the hosted zone. If you don\'t specify a value for Comment , Amazon Route 53 deletes the existing value of the Comment element, if any.

    :rtype: dict

ReturnsResponse Syntax
{
    'HostedZone': {
        'Id': 'string',
        'Name': 'string',
        'CallerReference': 'string',
        'Config': {
            'Comment': 'string',
            'PrivateZone': True|False
        },
        'ResourceRecordSetCount': 123,
        'LinkedService': {
            'ServicePrincipal': 'string',
            'Description': 'string'
        }
    }
}


Response Structure

(dict) --
A complex type that contains the response to the UpdateHostedZoneComment request.

HostedZone (dict) --
A complex type that contains the response to the UpdateHostedZoneComment request.

Id (string) --
The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name (string) --
The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than a-z , 0-9 , and - (hyphen) and how to specify internationalized domain names, see CreateHostedZone .

CallerReference (string) --
The value that you specified for CallerReference when you created the hosted zone.

Config (dict) --
A complex type that includes the Comment and PrivateZone elements. If you omitted the HostedZoneConfig and Comment elements from the request, the Config and Comment elements don\'t appear in the response.

Comment (string) --
Any comments that you want to include about the hosted zone.

PrivateZone (boolean) --
A value that indicates whether this is a private hosted zone.



ResourceRecordSetCount (integer) --
The number of resource record sets in the hosted zone.

LinkedService (dict) --
If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53.

ServicePrincipal (string) --
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.

Description (string) --
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53.











Exceptions

Route53.Client.exceptions.NoSuchHostedZone
Route53.Client.exceptions.InvalidInput


    :return: {
        'HostedZone': {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.NoSuchHostedZone
    Route53.Client.exceptions.InvalidInput
    
    """
    pass

def update_traffic_policy_comment(Id=None, Version=None, Comment=None):
    """
    Updates the comment for a specified traffic policy version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_traffic_policy_comment(
        Id='string',
        Version=123,
        Comment='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe value of Id for the traffic policy that you want to update the comment for.\n

    :type Version: integer
    :param Version: [REQUIRED]\nThe value of Version for the traffic policy that you want to update the comment for.\n

    :type Comment: string
    :param Comment: [REQUIRED]\nThe new comment for the specified traffic policy and version.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicy': {
        'Id': 'string',
        'Version': 123,
        'Name': 'string',
        'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        'Document': 'string',
        'Comment': 'string'
    }
}


Response Structure

(dict) --
A complex type that contains the response information for the traffic policy.

TrafficPolicy (dict) --
A complex type that contains settings for the specified traffic policy.

Id (string) --
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

Version (integer) --
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of Version is always 1.

Name (string) --
The name that you specified when you created the traffic policy.

Type (string) --
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

Document (string) --
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the CreateTrafficPolicy request. For more information about the JSON format, see Traffic Policy Document Format .

Comment (string) --
The comment that you specify in the CreateTrafficPolicy request, if any.









Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.ConcurrentModification


    :return: {
        'TrafficPolicy': {
            'Id': 'string',
            'Version': 123,
            'Name': 'string',
            'Type': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
            'Document': 'string',
            'Comment': 'string'
        }
    }
    
    
    :returns: 
    Route53.Client.exceptions.InvalidInput
    Route53.Client.exceptions.NoSuchTrafficPolicy
    Route53.Client.exceptions.ConcurrentModification
    
    """
    pass

def update_traffic_policy_instance(Id=None, TTL=None, TrafficPolicyId=None, TrafficPolicyVersion=None):
    """
    Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.
    When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_traffic_policy_instance(
        Id='string',
        TTL=123,
        TrafficPolicyId='string',
        TrafficPolicyVersion=123
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID of the traffic policy instance that you want to update.\n

    :type TTL: integer
    :param TTL: [REQUIRED]\nThe TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.\n

    :type TrafficPolicyId: string
    :param TrafficPolicyId: [REQUIRED]\nThe ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.\n

    :type TrafficPolicyVersion: integer
    :param TrafficPolicyVersion: [REQUIRED]\nThe version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrafficPolicyInstance': {
        'Id': 'string',
        'HostedZoneId': 'string',
        'Name': 'string',
        'TTL': 123,
        'State': 'string',
        'Message': 'string',
        'TrafficPolicyId': 'string',
        'TrafficPolicyVersion': 123,
        'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
    }
}


Response Structure

(dict) --
A complex type that contains information about the resource record sets that Amazon Route 53 created based on a specified traffic policy.

TrafficPolicyInstance (dict) --
A complex type that contains settings for the updated traffic policy instance.

Id (string) --
The ID that Amazon Route 53 assigned to the new traffic policy instance.

HostedZoneId (string) --
The ID of the hosted zone that Amazon Route 53 created resource record sets in.

Name (string) --
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.

TTL (integer) --
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.

State (string) --
The value of State is one of the following values:

Applied

Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.

Creating

Route 53 is creating the resource record sets. Use GetTrafficPolicyInstance to confirm that the CreateTrafficPolicyInstance request completed successfully.

Failed

Route 53 wasn\'t able to create or update the resource record sets. When the value of State is Failed , see Message for an explanation of what caused the request to fail.

Message (string) --
If State is Failed , an explanation of the reason for the failure. If State is another value, Message is empty.

TrafficPolicyId (string) --
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyVersion (integer) --
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.

TrafficPolicyType (string) --
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.









Exceptions

Route53.Client.exceptions.InvalidInput
Route53.Client.exceptions.NoSuchTrafficPolicy
Route53.Client.exceptions.NoSuchTrafficPolicyInstance
Route53.Client.exceptions.PriorRequestNotComplete
Route53.Client.exceptions.ConflictingTypes


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
            'TrafficPolicyType': 'SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA'
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

