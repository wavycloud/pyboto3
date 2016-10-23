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


def build_suggesters(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            Return typedict
            ReturnsResponse Syntax{
              'FieldNames': [
                'string',
              ]
            }
            Response Structure
            (dict) --The result of a BuildSuggester request. Contains a list of the fields used for suggestions.
            FieldNames (list) --A list of field names.
            (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            
            
            
    :type DomainName: string
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


def create_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            A name for the domain you are creating. Allowed characters are a-z (lower-case letters), 0-9, and hyphen (-). Domain names must start with a letter or number and be at least 3 and no more than 28 characters long.
            Return typedict
            ReturnsResponse Syntax{
              'DomainStatus': {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'DocService': {
                  'Endpoint': 'string'
                },
                'SearchService': {
                  'Endpoint': 'string'
                },
                'RequiresIndexDocuments': True|False,
                'Processing': True|False,
                'SearchInstanceType': 'string',
                'SearchPartitionCount': 123,
                'SearchInstanceCount': 123,
                'Limits': {
                  'MaximumReplicationCount': 123,
                  'MaximumPartitionCount': 123
                }
              }
            }
            Response Structure
            (dict) --The result of a CreateDomainRequest . Contains the status of a newly created domain.
            DomainStatus (dict) --The current status of the search domain.
            DomainId (string) --An internally generated unique identifier for a domain.
            DomainName (string) --A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon Resource Name (ARN) of the search domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --True if the search domain is created. It can take several minutes to initialize a domain when CreateDomain is called. Newly created search domains are returned from DescribeDomains with a false value for Created until domain creation is complete.
            Deleted (boolean) --True if the search domain has been deleted. The system must clean up resources dedicated to the search domain when DeleteDomain is called. Newly deleted search domains are returned from DescribeDomains with a true value for IsDeleted for several minutes until resource cleanup is complete.
            DocService (dict) --The service endpoint for updating documents in a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            SearchService (dict) --The service endpoint for requesting search results from a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            RequiresIndexDocuments (boolean) --True if IndexDocuments needs to be called to activate the current domain configuration.
            Processing (boolean) --True if processing is being done to activate the current domain configuration.
            SearchInstanceType (string) --The instance type that is being used to process search requests.
            SearchPartitionCount (integer) --The number of partitions across which the search index is spread.
            SearchInstanceCount (integer) --The number of search instances that are available to process search requests.
            Limits (dict) --
            MaximumReplicationCount (integer) --
            MaximumPartitionCount (integer) --
            
            
            
    :type DomainName: string
    """
    pass


def define_analysis_scheme(DomainName=None, AnalysisScheme=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param AnalysisScheme: [REQUIRED]
            Configuration information for an analysis scheme. Each analysis scheme has a unique name and specifies the language of the text to be processed. The following options can be configured for an analysis scheme: Synonyms , Stopwords , StemmingDictionary , JapaneseTokenizationDictionary and AlgorithmicStemming .
            AnalysisSchemeName (string) -- [REQUIRED]Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            AnalysisSchemeLanguage (string) -- [REQUIRED]An IETF RFC 4646 language code or mul for multiple languages.
            AnalysisOptions (dict) --Synonyms, stopwords, and stemming options for an analysis scheme. Includes tokenization dictionary for Japanese.
            Synonyms (string) --A JSON object that defines synonym groups and aliases. A synonym group is an array of arrays, where each sub-array is a group of terms where each term in the group is considered a synonym of every other term in the group. The aliases value is an object that contains a collection of string:value pairs where the string specifies a term and the array of values specifies each of the aliases for that term. An alias is considered a synonym of the specified term, but the term is not considered a synonym of the alias. For more information about specifying synonyms, see Synonyms in the Amazon CloudSearch Developer Guide .
            Stopwords (string) --A JSON array of terms to ignore during indexing and searching. For example, ['a', 'an', 'the', 'of'] . The stopwords dictionary must explicitly list each word you want to ignore. Wildcards and regular expressions are not supported.
            StemmingDictionary (string) --A JSON object that contains a collection of string:value pairs that each map a term to its stem. For example, {'term1': 'stem1', 'term2': 'stem2', 'term3': 'stem3'} . The stemming dictionary is applied in addition to any algorithmic stemming. This enables you to override the results of the algorithmic stemming to correct specific cases of overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.
            JapaneseTokenizationDictionary (string) --A JSON array that contains a collection of terms, tokens, readings and part of speech for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override the default tokenization for selected terms. This is only valid for Japanese language fields.
            AlgorithmicStemming (string) --The level of algorithmic stemming to perform: none , minimal , light , or full . The available levels vary depending on the language. For more information, see Language Specific Text Processing Settings in the Amazon CloudSearch Developer Guide
            
            
    :type AnalysisScheme: dict
    """
    pass


def define_expression(DomainName=None, Expression=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param Expression: [REQUIRED]
            A named expression that can be evaluated at search time. Can be used to sort the search results, define other expressions, or return computed information in the search results.
            ExpressionName (string) -- [REQUIRED]Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            ExpressionValue (string) -- [REQUIRED]The expression to evaluate for sorting while processing a search request. The Expression syntax is based on JavaScript expressions. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
            
    :type Expression: dict
    """
    pass


def define_index_field(DomainName=None, IndexField=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param IndexField: [REQUIRED]
            The index field and field options you want to configure.
            IndexFieldName (string) -- [REQUIRED]A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            IndexFieldType (string) -- [REQUIRED]The type of field. The valid options for a field depend on the field type. For more information about the supported field types, see Configuring Index Fields in the Amazon CloudSearch Developer Guide .
            IntOptions (dict) --Options for a 64-bit signed integer field. Present if IndexFieldType specifies the field is of type int . All options are enabled by default.
            DefaultValue (integer) -- A value to use for the field if the field isn't specified for a document. This can be important if you are using the field in an expression and that field is not present in every document.
            SourceField (string) --The name of the source field to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            DoubleOptions (dict) --Options for a double-precision 64-bit floating point field. Present if IndexFieldType specifies the field is of type double . All options are enabled by default.
            DefaultValue (float) --A value to use for the field if the field isn't specified for a document. This can be important if you are using the field in an expression and that field is not present in every document.
            SourceField (string) --The name of the source field to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            LiteralOptions (dict) --Options for literal field. Present if IndexFieldType specifies the field is of type literal . All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceField (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            TextOptions (dict) --Options for text field. Present if IndexFieldType specifies the field is of type text . A text field is always searchable. All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceField (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            HighlightEnabled (boolean) --Whether highlights can be returned for the field.
            AnalysisScheme (string) --The name of an analysis scheme for a text field.
            DateOptions (dict) --Options for a date field. Dates and times are specified in UTC (Coordinated Universal Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if IndexFieldType specifies the field is of type date . All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceField (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            LatLonOptions (dict) --Options for a latlon field. A latlon field contains a location stored as a latitude and longitude value pair. Present if IndexFieldType specifies the field is of type latlon . All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceField (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            SortEnabled (boolean) --Whether the field can be used to sort the search results.
            IntArrayOptions (dict) --Options for a field that contains an array of 64-bit signed integers. Present if IndexFieldType specifies the field is of type int-array . All options are enabled by default.
            DefaultValue (integer) -- A value to use for the field if the field isn't specified for a document.
            SourceFields (string) --A list of source fields to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            DoubleArrayOptions (dict) --Options for a field that contains an array of double-precision 64-bit floating point values. Present if IndexFieldType specifies the field is of type double-array . All options are enabled by default.
            DefaultValue (float) -- A value to use for the field if the field isn't specified for a document.
            SourceFields (string) --A list of source fields to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            LiteralArrayOptions (dict) --Options for a field that contains an array of literal strings. Present if IndexFieldType specifies the field is of type literal-array . All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceFields (string) --A list of source fields to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            TextArrayOptions (dict) --Options for a field that contains an array of text strings. Present if IndexFieldType specifies the field is of type text-array . A text-array field is always searchable. All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceFields (string) --A list of source fields to map to the field.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            HighlightEnabled (boolean) --Whether highlights can be returned for the field.
            AnalysisScheme (string) --The name of an analysis scheme for a text-array field.
            DateArrayOptions (dict) --Options for a field that contains an array of dates. Present if IndexFieldType specifies the field is of type date-array . All options are enabled by default.
            DefaultValue (string) -- A value to use for the field if the field isn't specified for a document.
            SourceFields (string) --A list of source fields to map to the field.
            FacetEnabled (boolean) --Whether facet information can be returned for the field.
            SearchEnabled (boolean) --Whether the contents of the field are searchable.
            ReturnEnabled (boolean) --Whether the contents of the field can be returned in the search results.
            
            
    :type IndexField: dict
    """
    pass


def define_suggester(DomainName=None, Suggester=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param Suggester: [REQUIRED]
            Configuration information for a search suggester. Each suggester has a unique name and specifies the text field you want to use for suggestions. The following options can be configured for a suggester: FuzzyMatching , SortExpression .
            SuggesterName (string) -- [REQUIRED]Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            DocumentSuggesterOptions (dict) -- [REQUIRED]Options for a search suggester.
            SourceField (string) -- [REQUIRED]The name of the index field you want to use for suggestions.
            FuzzyMatching (string) --The level of fuzziness allowed when suggesting matches for a string: none , low , or high . With none, the specified string is treated as an exact prefix. With low, suggestions must differ from the specified string by no more than one character. With high, suggestions can differ by up to two characters. The default is none.
            SortExpression (string) --An expression that computes a score for each suggestion to control how they are sorted. The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so sort expressions cannot reference the _score value. To sort suggestions using a numeric field or existing expression, simply specify the name of the field or expression. If no expression is configured for the suggester, the suggestions are sorted with the closest matches listed first.
            
            
    :type Suggester: dict
    """
    pass


def delete_analysis_scheme(DomainName=None, AnalysisSchemeName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param AnalysisSchemeName: [REQUIRED]
            The name of the analysis scheme you want to delete.
            
    :type AnalysisSchemeName: string
    """
    pass


def delete_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to permanently delete.
            Return typedict
            ReturnsResponse Syntax{
              'DomainStatus': {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'DocService': {
                  'Endpoint': 'string'
                },
                'SearchService': {
                  'Endpoint': 'string'
                },
                'RequiresIndexDocuments': True|False,
                'Processing': True|False,
                'SearchInstanceType': 'string',
                'SearchPartitionCount': 123,
                'SearchInstanceCount': 123,
                'Limits': {
                  'MaximumReplicationCount': 123,
                  'MaximumPartitionCount': 123
                }
              }
            }
            Response Structure
            (dict) --The result of a DeleteDomain request. Contains the status of a newly deleted domain, or no status if the domain has already been completely deleted.
            DomainStatus (dict) --The current status of the search domain.
            DomainId (string) --An internally generated unique identifier for a domain.
            DomainName (string) --A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon Resource Name (ARN) of the search domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --True if the search domain is created. It can take several minutes to initialize a domain when CreateDomain is called. Newly created search domains are returned from DescribeDomains with a false value for Created until domain creation is complete.
            Deleted (boolean) --True if the search domain has been deleted. The system must clean up resources dedicated to the search domain when DeleteDomain is called. Newly deleted search domains are returned from DescribeDomains with a true value for IsDeleted for several minutes until resource cleanup is complete.
            DocService (dict) --The service endpoint for updating documents in a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            SearchService (dict) --The service endpoint for requesting search results from a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            RequiresIndexDocuments (boolean) --True if IndexDocuments needs to be called to activate the current domain configuration.
            Processing (boolean) --True if processing is being done to activate the current domain configuration.
            SearchInstanceType (string) --The instance type that is being used to process search requests.
            SearchPartitionCount (integer) --The number of partitions across which the search index is spread.
            SearchInstanceCount (integer) --The number of search instances that are available to process search requests.
            Limits (dict) --
            MaximumReplicationCount (integer) --
            MaximumPartitionCount (integer) --
            
            
            
    :type DomainName: string
    """
    pass


def delete_expression(DomainName=None, ExpressionName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param ExpressionName: [REQUIRED]
            The name of the `` Expression`` to delete.
            
    :type ExpressionName: string
    """
    pass


def delete_index_field(DomainName=None, IndexFieldName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param IndexFieldName: [REQUIRED]
            The name of the index field your want to remove from the domain's indexing options.
            
    :type IndexFieldName: string
    """
    pass


def delete_suggester(DomainName=None, SuggesterName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param SuggesterName: [REQUIRED]
            Specifies the name of the suggester you want to delete.
            
    :type SuggesterName: string
    """
    pass


def describe_analysis_schemes(DomainName=None, AnalysisSchemeNames=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param AnalysisSchemeNames: The analysis schemes you want to describe.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            
    :type AnalysisSchemeNames: list
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
    """
    pass


def describe_availability_options(DomainName=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
    """
    pass


def describe_domains(DomainNames=None):
    """
    :param DomainNames: The names of the domains you want to include in the response.
            (string) --A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            Return typedict
            ReturnsResponse Syntax{
              'DomainStatusList': [
                {
                  'DomainId': 'string',
                  'DomainName': 'string',
                  'ARN': 'string',
                  'Created': True|False,
                  'Deleted': True|False,
                  'DocService': {
                    'Endpoint': 'string'
                  },
                  'SearchService': {
                    'Endpoint': 'string'
                  },
                  'RequiresIndexDocuments': True|False,
                  'Processing': True|False,
                  'SearchInstanceType': 'string',
                  'SearchPartitionCount': 123,
                  'SearchInstanceCount': 123,
                  'Limits': {
                    'MaximumReplicationCount': 123,
                    'MaximumPartitionCount': 123
                  }
                },
              ]
            }
            Response Structure
            (dict) --The result of a DescribeDomains request. Contains the status of the domains specified in the request or all domains owned by the account.
            DomainStatusList (list) --A list that contains the status of each requested domain.
            (dict) --The current status of the search domain.
            DomainId (string) --An internally generated unique identifier for a domain.
            DomainName (string) --A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon Resource Name (ARN) of the search domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --True if the search domain is created. It can take several minutes to initialize a domain when CreateDomain is called. Newly created search domains are returned from DescribeDomains with a false value for Created until domain creation is complete.
            Deleted (boolean) --True if the search domain has been deleted. The system must clean up resources dedicated to the search domain when DeleteDomain is called. Newly deleted search domains are returned from DescribeDomains with a true value for IsDeleted for several minutes until resource cleanup is complete.
            DocService (dict) --The service endpoint for updating documents in a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            SearchService (dict) --The service endpoint for requesting search results from a search domain.
            Endpoint (string) --The endpoint to which service requests can be submitted. For example, search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com or doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com .
            RequiresIndexDocuments (boolean) --True if IndexDocuments needs to be called to activate the current domain configuration.
            Processing (boolean) --True if processing is being done to activate the current domain configuration.
            SearchInstanceType (string) --The instance type that is being used to process search requests.
            SearchPartitionCount (integer) --The number of partitions across which the search index is spread.
            SearchInstanceCount (integer) --The number of search instances that are available to process search requests.
            Limits (dict) --
            MaximumReplicationCount (integer) --
            MaximumPartitionCount (integer) --
            
            
            
    :type DomainNames: list
    """
    pass


def describe_expressions(DomainName=None, ExpressionNames=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param ExpressionNames: Limits the `` DescribeExpressions`` response to the specified expressions. If not specified, all expressions are shown.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            
    :type ExpressionNames: list
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
    """
    pass


def describe_index_fields(DomainName=None, FieldNames=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param FieldNames: A list of the index fields you want to describe. If not specified, information is returned for all configured index fields.
            (string) --
            
    :type FieldNames: list
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
    """
    pass


def describe_scaling_parameters(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            Return typedict
            ReturnsResponse Syntax{
              'ScalingParameters': {
                'Options': {
                  'DesiredInstanceType': 'search.m1.small'|'search.m1.large'|'search.m2.xlarge'|'search.m2.2xlarge'|'search.m3.medium'|'search.m3.large'|'search.m3.xlarge'|'search.m3.2xlarge',
                  'DesiredReplicationCount': 123,
                  'DesiredPartitionCount': 123
                },
                'Status': {
                  'CreationDate': datetime(2015, 1, 1),
                  'UpdateDate': datetime(2015, 1, 1),
                  'UpdateVersion': 123,
                  'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                  'PendingDeletion': True|False
                }
              }
            }
            Response Structure
            (dict) --The result of a DescribeScalingParameters request. Contains the scaling parameters configured for the domain specified in the request.
            ScalingParameters (dict) --The status and configuration of a search domain's scaling parameters.
            Options (dict) --The desired instance type and desired number of replicas of each index partition.
            DesiredInstanceType (string) --The instance type that you want to preconfigure for your domain. For example, search.m1.small .
            DesiredReplicationCount (integer) --The number of replicas you want to preconfigure for each index partition.
            DesiredPartitionCount (integer) --The number of partitions you want to preconfigure for your domain. Only valid when you select m2.2xlarge as the desired instance type.
            Status (dict) --The status of domain configuration option.
            CreationDate (datetime) --A timestamp for when this option was created.
            UpdateDate (datetime) --A timestamp for when this option was last updated.
            UpdateVersion (integer) --A unique integer that indicates when this option was last updated.
            State (string) --The state of processing a change to an option. Possible values:
            RequiresIndexDocuments : the option's latest value will not be deployed until IndexDocuments has been called and indexing is complete.
            Processing : the option's latest value is in the process of being activated.
            Active : the option's latest value is completely deployed.
            FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
            PendingDeletion (boolean) --Indicates that the option will be deleted once processing is complete.
            
            
            
    :type DomainName: string
    """
    pass


def describe_service_access_policies(DomainName=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
    """
    pass


def describe_suggesters(DomainName=None, SuggesterNames=None, Deployed=None):
    """
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            
    :type DomainName: string
    :param SuggesterNames: The suggesters you want to describe.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            
    :type SuggesterNames: list
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .
    :type Deployed: boolean
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


def index_documents(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            Return typedict
            ReturnsResponse Syntax{
              'FieldNames': [
                'string',
              ]
            }
            Response Structure
            (dict) --The result of an IndexDocuments request. Contains the status of the indexing operation, including the fields being indexed.
            FieldNames (list) --The names of the fields that are currently being indexed.
            (string) --A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options.
            Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.
            The name score is reserved and cannot be used as a field name. To reference a document's ID, you can use the name _id .
            
            
            
    :type DomainName: string
    """
    pass


def list_domain_names():
    """
    """
    pass


def update_availability_options(DomainName=None, MultiAZ=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param MultiAZ: [REQUIRED]
            You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to false .
            
    :type MultiAZ: boolean
    """
    pass


def update_scaling_parameters(DomainName=None, ScalingParameters=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param ScalingParameters: [REQUIRED]
            The desired instance type and desired number of replicas of each index partition.
            DesiredInstanceType (string) --The instance type that you want to preconfigure for your domain. For example, search.m1.small .
            DesiredReplicationCount (integer) --The number of replicas you want to preconfigure for each index partition.
            DesiredPartitionCount (integer) --The number of partitions you want to preconfigure for your domain. Only valid when you select m2.2xlarge as the desired instance type.
            
    :type ScalingParameters: dict
    """
    pass


def update_service_access_policies(DomainName=None, AccessPolicies=None):
    """
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param AccessPolicies: [REQUIRED]
            The access rules you want to configure. These rules replace any existing rules.
            
    :type AccessPolicies: string
    """
    pass
