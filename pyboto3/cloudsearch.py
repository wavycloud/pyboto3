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

def build_suggesters(DomainName=None):
    """
    Indexes the search suggestions. For more information, see Configuring Suggesters in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.build_suggesters(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
        'FieldNames': [
            'string',
        ]
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

def create_domain(DomainName=None):
    """
    Creates a new search domain. For more information, see Creating a Search Domain in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A name for the domain you are creating. Allowed characters are a-z (lower-case letters), 0-9, and hyphen (-). Domain names must start with a letter or number and be at least 3 and no more than 28 characters long.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def define_analysis_scheme(DomainName=None, AnalysisScheme=None):
    """
    Configures an analysis scheme that can be applied to a text or text-array field to define language-specific text processing options. For more information, see Configuring Analysis Schemes in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.define_analysis_scheme(
        DomainName='string',
        AnalysisScheme={
            'AnalysisSchemeName': 'string',
            'AnalysisSchemeLanguage': 'ar'|'bg'|'ca'|'cs'|'da'|'de'|'el'|'en'|'es'|'eu'|'fa'|'fi'|'fr'|'ga'|'gl'|'he'|'hi'|'hu'|'hy'|'id'|'it'|'ja'|'ko'|'lv'|'mul'|'nl'|'no'|'pt'|'ro'|'ru'|'sv'|'th'|'tr'|'zh-Hans'|'zh-Hant',
            'AnalysisOptions': {
                'Synonyms': 'string',
                'Stopwords': 'string',
                'StemmingDictionary': 'string',
                'JapaneseTokenizationDictionary': 'string',
                'AlgorithmicStemming': 'none'|'minimal'|'light'|'full'
            }
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type AnalysisScheme: dict
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
            
            

    :rtype: dict
    :return: {
        'AnalysisScheme': {
            'Options': {
                'AnalysisSchemeName': 'string',
                'AnalysisSchemeLanguage': 'ar'|'bg'|'ca'|'cs'|'da'|'de'|'el'|'en'|'es'|'eu'|'fa'|'fi'|'fr'|'ga'|'gl'|'he'|'hi'|'hu'|'hy'|'id'|'it'|'ja'|'ko'|'lv'|'mul'|'nl'|'no'|'pt'|'ro'|'ru'|'sv'|'th'|'tr'|'zh-Hans'|'zh-Hant',
                'AnalysisOptions': {
                    'Synonyms': 'string',
                    'Stopwords': 'string',
                    'StemmingDictionary': 'string',
                    'JapaneseTokenizationDictionary': 'string',
                    'AlgorithmicStemming': 'none'|'minimal'|'light'|'full'
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def define_expression(DomainName=None, Expression=None):
    """
    Configures an `` Expression`` for the search domain. Used to create new expressions and modify existing ones. If the expression exists, the new configuration replaces the old one. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.define_expression(
        DomainName='string',
        Expression={
            'ExpressionName': 'string',
            'ExpressionValue': 'string'
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type Expression: dict
    :param Expression: [REQUIRED]
            A named expression that can be evaluated at search time. Can be used to sort the search results, define other expressions, or return computed information in the search results.
            ExpressionName (string) -- [REQUIRED]Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            ExpressionValue (string) -- [REQUIRED]The expression to evaluate for sorting while processing a search request. The Expression syntax is based on JavaScript expressions. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
            

    :rtype: dict
    :return: {
        'Expression': {
            'Options': {
                'ExpressionName': 'string',
                'ExpressionValue': 'string'
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def define_index_field(DomainName=None, IndexField=None):
    """
    Configures an `` IndexField`` for the search domain. Used to create new fields and modify existing ones. You must specify the name of the domain you are configuring and an index field configuration. The index field configuration specifies a unique name, the index field type, and the options you want to configure for the field. The options you can specify depend on the `` IndexFieldType`` . If the field exists, the new configuration replaces the old one. For more information, see Configuring Index Fields in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.define_index_field(
        DomainName='string',
        IndexField={
            'IndexFieldName': 'string',
            'IndexFieldType': 'int'|'double'|'literal'|'text'|'date'|'latlon'|'int-array'|'double-array'|'literal-array'|'text-array'|'date-array',
            'IntOptions': {
                'DefaultValue': 123,
                'SourceField': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False,
                'SortEnabled': True|False
            },
            'DoubleOptions': {
                'DefaultValue': 123.0,
                'SourceField': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False,
                'SortEnabled': True|False
            },
            'LiteralOptions': {
                'DefaultValue': 'string',
                'SourceField': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False,
                'SortEnabled': True|False
            },
            'TextOptions': {
                'DefaultValue': 'string',
                'SourceField': 'string',
                'ReturnEnabled': True|False,
                'SortEnabled': True|False,
                'HighlightEnabled': True|False,
                'AnalysisScheme': 'string'
            },
            'DateOptions': {
                'DefaultValue': 'string',
                'SourceField': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False,
                'SortEnabled': True|False
            },
            'LatLonOptions': {
                'DefaultValue': 'string',
                'SourceField': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False,
                'SortEnabled': True|False
            },
            'IntArrayOptions': {
                'DefaultValue': 123,
                'SourceFields': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False
            },
            'DoubleArrayOptions': {
                'DefaultValue': 123.0,
                'SourceFields': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False
            },
            'LiteralArrayOptions': {
                'DefaultValue': 'string',
                'SourceFields': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False
            },
            'TextArrayOptions': {
                'DefaultValue': 'string',
                'SourceFields': 'string',
                'ReturnEnabled': True|False,
                'HighlightEnabled': True|False,
                'AnalysisScheme': 'string'
            },
            'DateArrayOptions': {
                'DefaultValue': 'string',
                'SourceFields': 'string',
                'FacetEnabled': True|False,
                'SearchEnabled': True|False,
                'ReturnEnabled': True|False
            }
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type IndexField: dict
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
            
            

    :rtype: dict
    :return: {
        'IndexField': {
            'Options': {
                'IndexFieldName': 'string',
                'IndexFieldType': 'int'|'double'|'literal'|'text'|'date'|'latlon'|'int-array'|'double-array'|'literal-array'|'text-array'|'date-array',
                'IntOptions': {
                    'DefaultValue': 123,
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'DoubleOptions': {
                    'DefaultValue': 123.0,
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'LiteralOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'TextOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False,
                    'HighlightEnabled': True|False,
                    'AnalysisScheme': 'string'
                },
                'DateOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'LatLonOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'IntArrayOptions': {
                    'DefaultValue': 123,
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'DoubleArrayOptions': {
                    'DefaultValue': 123.0,
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'LiteralArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'TextArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'ReturnEnabled': True|False,
                    'HighlightEnabled': True|False,
                    'AnalysisScheme': 'string'
                },
                'DateArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def define_suggester(DomainName=None, Suggester=None):
    """
    Configures a suggester for a domain. A suggester enables you to display possible matches before users finish typing their queries. When you configure a suggester, you must specify the name of the text field you want to search for possible matches and a unique name for the suggester. For more information, see Getting Search Suggestions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.define_suggester(
        DomainName='string',
        Suggester={
            'SuggesterName': 'string',
            'DocumentSuggesterOptions': {
                'SourceField': 'string',
                'FuzzyMatching': 'none'|'low'|'high',
                'SortExpression': 'string'
            }
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type Suggester: dict
    :param Suggester: [REQUIRED]
            Configuration information for a search suggester. Each suggester has a unique name and specifies the text field you want to use for suggestions. The following options can be configured for a suggester: FuzzyMatching , SortExpression .
            SuggesterName (string) -- [REQUIRED]Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            DocumentSuggesterOptions (dict) -- [REQUIRED]Options for a search suggester.
            SourceField (string) -- [REQUIRED]The name of the index field you want to use for suggestions.
            FuzzyMatching (string) --The level of fuzziness allowed when suggesting matches for a string: none , low , or high . With none, the specified string is treated as an exact prefix. With low, suggestions must differ from the specified string by no more than one character. With high, suggestions can differ by up to two characters. The default is none.
            SortExpression (string) --An expression that computes a score for each suggestion to control how they are sorted. The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so sort expressions cannot reference the _score value. To sort suggestions using a numeric field or existing expression, simply specify the name of the field or expression. If no expression is configured for the suggester, the suggestions are sorted with the closest matches listed first.
            
            

    :rtype: dict
    :return: {
        'Suggester': {
            'Options': {
                'SuggesterName': 'string',
                'DocumentSuggesterOptions': {
                    'SourceField': 'string',
                    'FuzzyMatching': 'none'|'low'|'high',
                    'SortExpression': 'string'
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def delete_analysis_scheme(DomainName=None, AnalysisSchemeName=None):
    """
    Deletes an analysis scheme. For more information, see Configuring Analysis Schemes in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_analysis_scheme(
        DomainName='string',
        AnalysisSchemeName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type AnalysisSchemeName: string
    :param AnalysisSchemeName: [REQUIRED]
            The name of the analysis scheme you want to delete.
            

    :rtype: dict
    :return: {
        'AnalysisScheme': {
            'Options': {
                'AnalysisSchemeName': 'string',
                'AnalysisSchemeLanguage': 'ar'|'bg'|'ca'|'cs'|'da'|'de'|'el'|'en'|'es'|'eu'|'fa'|'fi'|'fr'|'ga'|'gl'|'he'|'hi'|'hu'|'hy'|'id'|'it'|'ja'|'ko'|'lv'|'mul'|'nl'|'no'|'pt'|'ro'|'ru'|'sv'|'th'|'tr'|'zh-Hans'|'zh-Hant',
                'AnalysisOptions': {
                    'Synonyms': 'string',
                    'Stopwords': 'string',
                    'StemmingDictionary': 'string',
                    'JapaneseTokenizationDictionary': 'string',
                    'AlgorithmicStemming': 'none'|'minimal'|'light'|'full'
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def delete_domain(DomainName=None):
    """
    Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see Deleting a Search Domain in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to permanently delete.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def delete_expression(DomainName=None, ExpressionName=None):
    """
    Removes an `` Expression`` from the search domain. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_expression(
        DomainName='string',
        ExpressionName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type ExpressionName: string
    :param ExpressionName: [REQUIRED]
            The name of the `` Expression`` to delete.
            

    :rtype: dict
    :return: {
        'Expression': {
            'Options': {
                'ExpressionName': 'string',
                'ExpressionValue': 'string'
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def delete_index_field(DomainName=None, IndexFieldName=None):
    """
    Removes an `` IndexField`` from the search domain. For more information, see Configuring Index Fields in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_index_field(
        DomainName='string',
        IndexFieldName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type IndexFieldName: string
    :param IndexFieldName: [REQUIRED]
            The name of the index field your want to remove from the domain's indexing options.
            

    :rtype: dict
    :return: {
        'IndexField': {
            'Options': {
                'IndexFieldName': 'string',
                'IndexFieldType': 'int'|'double'|'literal'|'text'|'date'|'latlon'|'int-array'|'double-array'|'literal-array'|'text-array'|'date-array',
                'IntOptions': {
                    'DefaultValue': 123,
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'DoubleOptions': {
                    'DefaultValue': 123.0,
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'LiteralOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'TextOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False,
                    'HighlightEnabled': True|False,
                    'AnalysisScheme': 'string'
                },
                'DateOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'LatLonOptions': {
                    'DefaultValue': 'string',
                    'SourceField': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False,
                    'SortEnabled': True|False
                },
                'IntArrayOptions': {
                    'DefaultValue': 123,
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'DoubleArrayOptions': {
                    'DefaultValue': 123.0,
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'LiteralArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                },
                'TextArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'ReturnEnabled': True|False,
                    'HighlightEnabled': True|False,
                    'AnalysisScheme': 'string'
                },
                'DateArrayOptions': {
                    'DefaultValue': 'string',
                    'SourceFields': 'string',
                    'FacetEnabled': True|False,
                    'SearchEnabled': True|False,
                    'ReturnEnabled': True|False
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def delete_suggester(DomainName=None, SuggesterName=None):
    """
    Deletes a suggester. For more information, see Getting Search Suggestions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_suggester(
        DomainName='string',
        SuggesterName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type SuggesterName: string
    :param SuggesterName: [REQUIRED]
            Specifies the name of the suggester you want to delete.
            

    :rtype: dict
    :return: {
        'Suggester': {
            'Options': {
                'SuggesterName': 'string',
                'DocumentSuggesterOptions': {
                    'SourceField': 'string',
                    'FuzzyMatching': 'none'|'low'|'high',
                    'SortExpression': 'string'
                }
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_analysis_schemes(DomainName=None, AnalysisSchemeNames=None, Deployed=None):
    """
    Gets the analysis schemes configured for a domain. An analysis scheme defines language-specific text processing options for a text field. Can be limited to specific analysis schemes by name. By default, shows all analysis schemes and includes any pending changes to the configuration. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Configuring Analysis Schemes in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_analysis_schemes(
        DomainName='string',
        AnalysisSchemeNames=[
            'string',
        ],
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type AnalysisSchemeNames: list
    :param AnalysisSchemeNames: The analysis schemes you want to describe.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'AnalysisSchemes': [
            {
                'Options': {
                    'AnalysisSchemeName': 'string',
                    'AnalysisSchemeLanguage': 'ar'|'bg'|'ca'|'cs'|'da'|'de'|'el'|'en'|'es'|'eu'|'fa'|'fi'|'fr'|'ga'|'gl'|'he'|'hi'|'hu'|'hy'|'id'|'it'|'ja'|'ko'|'lv'|'mul'|'nl'|'no'|'pt'|'ro'|'ru'|'sv'|'th'|'tr'|'zh-Hans'|'zh-Hant',
                    'AnalysisOptions': {
                        'Synonyms': 'string',
                        'Stopwords': 'string',
                        'StemmingDictionary': 'string',
                        'JapaneseTokenizationDictionary': 'string',
                        'AlgorithmicStemming': 'none'|'minimal'|'light'|'full'
                    }
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                    'PendingDeletion': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_availability_options(DomainName=None, Deployed=None):
    """
    Gets the availability options configured for a domain. By default, shows the configuration with any pending changes. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Configuring Availability Options in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_availability_options(
        DomainName='string',
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'AvailabilityOptions': {
            'Options': True|False,
            'Status': {
                'CreationDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'UpdateVersion': 123,
                'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                'PendingDeletion': True|False
            }
        }
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_domains(DomainNames=None):
    """
    Gets information about the search domains owned by this account. Can be limited to specific domains. Shows all domains by default. To get the number of searchable documents in a domain, use the console or submit a matchall request to your domain's search endpoint: q=matchallamp;q.parser=structuredamp;size=0 . For more information, see Getting Information about a Search Domain in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_domains(
        DomainNames=[
            'string',
        ]
    )
    
    
    :type DomainNames: list
    :param DomainNames: The names of the domains you want to include in the response.
            (string) --A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_expressions(DomainName=None, ExpressionNames=None, Deployed=None):
    """
    Gets the expressions configured for the search domain. Can be limited to specific expressions by name. By default, shows all expressions and includes any pending changes to the configuration. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_expressions(
        DomainName='string',
        ExpressionNames=[
            'string',
        ],
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type ExpressionNames: list
    :param ExpressionNames: Limits the `` DescribeExpressions`` response to the specified expressions. If not specified, all expressions are shown.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'Expressions': [
            {
                'Options': {
                    'ExpressionName': 'string',
                    'ExpressionValue': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                    'PendingDeletion': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_index_fields(DomainName=None, FieldNames=None, Deployed=None):
    """
    Gets information about the index fields configured for the search domain. Can be limited to specific fields by name. By default, shows all fields and includes any pending changes to the configuration. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Getting Domain Information in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_index_fields(
        DomainName='string',
        FieldNames=[
            'string',
        ],
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type FieldNames: list
    :param FieldNames: A list of the index fields you want to describe. If not specified, information is returned for all configured index fields.
            (string) --
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'IndexFields': [
            {
                'Options': {
                    'IndexFieldName': 'string',
                    'IndexFieldType': 'int'|'double'|'literal'|'text'|'date'|'latlon'|'int-array'|'double-array'|'literal-array'|'text-array'|'date-array',
                    'IntOptions': {
                        'DefaultValue': 123,
                        'SourceField': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False
                    },
                    'DoubleOptions': {
                        'DefaultValue': 123.0,
                        'SourceField': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False
                    },
                    'LiteralOptions': {
                        'DefaultValue': 'string',
                        'SourceField': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False
                    },
                    'TextOptions': {
                        'DefaultValue': 'string',
                        'SourceField': 'string',
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False,
                        'HighlightEnabled': True|False,
                        'AnalysisScheme': 'string'
                    },
                    'DateOptions': {
                        'DefaultValue': 'string',
                        'SourceField': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False
                    },
                    'LatLonOptions': {
                        'DefaultValue': 'string',
                        'SourceField': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False,
                        'SortEnabled': True|False
                    },
                    'IntArrayOptions': {
                        'DefaultValue': 123,
                        'SourceFields': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False
                    },
                    'DoubleArrayOptions': {
                        'DefaultValue': 123.0,
                        'SourceFields': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False
                    },
                    'LiteralArrayOptions': {
                        'DefaultValue': 'string',
                        'SourceFields': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False
                    },
                    'TextArrayOptions': {
                        'DefaultValue': 'string',
                        'SourceFields': 'string',
                        'ReturnEnabled': True|False,
                        'HighlightEnabled': True|False,
                        'AnalysisScheme': 'string'
                    },
                    'DateArrayOptions': {
                        'DefaultValue': 'string',
                        'SourceFields': 'string',
                        'FacetEnabled': True|False,
                        'SearchEnabled': True|False,
                        'ReturnEnabled': True|False
                    }
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                    'PendingDeletion': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_scaling_parameters(DomainName=None):
    """
    Gets the scaling parameters configured for a domain. A domain's scaling parameters specify the desired search instance type and replication count. For more information, see Configuring Scaling Options in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scaling_parameters(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_service_access_policies(DomainName=None, Deployed=None):
    """
    Gets information about the access policies that control access to the domain's document and search endpoints. By default, shows the configuration with any pending changes. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Configuring Access for a Search Domain in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_service_access_policies(
        DomainName='string',
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'AccessPolicies': {
            'Options': 'string',
            'Status': {
                'CreationDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'UpdateVersion': 123,
                'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                'PendingDeletion': True|False
            }
        }
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def describe_suggesters(DomainName=None, SuggesterNames=None, Deployed=None):
    """
    Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the Deployed option to true to show the active configuration and exclude pending changes. For more information, see Getting Search Suggestions in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_suggesters(
        DomainName='string',
        SuggesterNames=[
            'string',
        ],
        Deployed=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain you want to describe.
            

    :type SuggesterNames: list
    :param SuggesterNames: The suggesters you want to describe.
            (string) --Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
            

    :type Deployed: boolean
    :param Deployed: Whether to display the deployed configuration (true ) or include any pending changes (false ). Defaults to false .

    :rtype: dict
    :return: {
        'Suggesters': [
            {
                'Options': {
                    'SuggesterName': 'string',
                    'DocumentSuggesterOptions': {
                        'SourceField': 'string',
                        'FuzzyMatching': 'none'|'low'|'high',
                        'SortExpression': 'string'
                    }
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                    'PendingDeletion': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
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

def get_waiter():
    """
    
    """
    pass

def index_documents(DomainName=None):
    """
    Tells the search domain to start indexing its documents using the latest indexing options. This operation must be invoked to activate options whose  OptionStatus is RequiresIndexDocuments .
    See also: AWS API Documentation
    
    
    :example: response = client.index_documents(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
        'FieldNames': [
            'string',
        ]
    }
    
    
    """
    pass

def list_domain_names():
    """
    Lists all search domains owned by an account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_domain_names()
    
    
    :rtype: dict
    :return: {
        'DomainNames': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def update_availability_options(DomainName=None, MultiAZ=None):
    """
    Configures the availability options for a domain. Enabling the Multi-AZ option expands an Amazon CloudSearch domain to an additional Availability Zone in the same Region to increase fault tolerance in the event of a service disruption. Changes to the Multi-AZ option can take about half an hour to become active. For more information, see Configuring Availability Options in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_availability_options(
        DomainName='string',
        MultiAZ=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type MultiAZ: boolean
    :param MultiAZ: [REQUIRED]
            You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to false .
            

    :rtype: dict
    :return: {
        'AvailabilityOptions': {
            'Options': True|False,
            'Status': {
                'CreationDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'UpdateVersion': 123,
                'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                'PendingDeletion': True|False
            }
        }
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def update_scaling_parameters(DomainName=None, ScalingParameters=None):
    """
    Configures scaling parameters for a domain. A domain's scaling parameters specify the desired search instance type and replication count. Amazon CloudSearch will still automatically scale your domain based on the volume of data and traffic, but not below the desired instance type and replication count. If the Multi-AZ option is enabled, these values control the resources used per Availability Zone. For more information, see Configuring Scaling Options in the Amazon CloudSearch Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_scaling_parameters(
        DomainName='string',
        ScalingParameters={
            'DesiredInstanceType': 'search.m1.small'|'search.m1.large'|'search.m2.xlarge'|'search.m2.2xlarge'|'search.m3.medium'|'search.m3.large'|'search.m3.xlarge'|'search.m3.2xlarge',
            'DesiredReplicationCount': 123,
            'DesiredPartitionCount': 123
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type ScalingParameters: dict
    :param ScalingParameters: [REQUIRED]
            The desired instance type and desired number of replicas of each index partition.
            DesiredInstanceType (string) --The instance type that you want to preconfigure for your domain. For example, search.m1.small .
            DesiredReplicationCount (integer) --The number of replicas you want to preconfigure for each index partition.
            DesiredPartitionCount (integer) --The number of partitions you want to preconfigure for your domain. Only valid when you select m2.2xlarge as the desired instance type.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

def update_service_access_policies(DomainName=None, AccessPolicies=None):
    """
    Configures the access rules that control access to the domain's document and search endpoints. For more information, see Configuring Access for an Amazon CloudSearch Domain .
    See also: AWS API Documentation
    
    
    :example: response = client.update_service_access_policies(
        DomainName='string',
        AccessPolicies='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type AccessPolicies: string
    :param AccessPolicies: [REQUIRED]
            The access rules you want to configure. These rules replace any existing rules.
            

    :rtype: dict
    :return: {
        'AccessPolicies': {
            'Options': 'string',
            'Status': {
                'CreationDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'UpdateVersion': 123,
                'State': 'RequiresIndexDocuments'|'Processing'|'Active'|'FailedToValidate',
                'PendingDeletion': True|False
            }
        }
    }
    
    
    :returns: 
    RequiresIndexDocuments : the option's latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
    Processing : the option's latest value is in the process of being activated.
    Active : the option's latest value is completely deployed.
    FailedToValidate : the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.
    
    """
    pass

