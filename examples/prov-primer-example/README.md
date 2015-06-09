This example is based off the examples contained within the [W3C PROV Primer]( http://www.w3.org/TR/prov-primer)

output:
```
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ex: <http://www.example.org#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:compile1> a prov:Activity .

<ex:analyst> a prov:Role .

<ex:composedData> a prov:Role .

<ex:dataToCompose> a prov:Role .

<ex:instructions> a prov:Entity,
        prov:Plan .

<ex:quoteInBlogEntry-20130326> a prov:Entity ;
    prov:wasDerivedFrom <ex:article> ;
    prov:wasInfluencedBy <ex:article> ;
    prov:wasQuotedFrom <ex:article> .

<ex:regionsToAggregateBy> a prov:Role .

<ex:article_v1> a prov:Entity ;
    prov:alternateOf <ex:article>,
        <ex:article_v2> ;
    prov:specializationOf <ex:article> .

<ex:article_v2> a prov:Entity ;
    prov:alternateOf <ex:article>,
        <ex:article_v1> ;
    prov:specializationOf <ex:article> .

<ex:chart2> a prov:Entity ;
    prov:generatedAtTime "2012-04-01T15:21:00"^^xsd:dateTime ;
    prov:wasDerivedFrom <ex:chart1>,
        <ex:dataset2> ;
    prov:wasInfluencedBy <ex:chart1>,
        <ex:dataset2> ;
    prov:wasRevisionOf <ex:chart1> .

<ex:chartgen> a prov:Agent,
        prov:Organization ;
    foaf:name "Chart Generators Inc" .

<ex:correct1> a prov:Activity ;
    prov:endedAtTime "2012-04-01T15:21:00"^^xsd:dateTime ;
    prov:generated <ex:dataset2> ;
    prov:influenced <ex:dataset2> ;
    prov:qualifiedAssociation [ a prov:Association,
                prov:Influence ;
            prov:agent <ex:edith> ;
            prov:hadPlan <ex:instructions> ;
            prov:influencer <ex:edith> ] ;
    prov:startedAtTime "2012-03-31T09:21:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <ex:edith> ;
    prov:wasInfluencedBy <ex:edith> .

<ex:composition1> a prov:Entity ;
    prov:influenced <ex:illustrate1> ;
    prov:qualifiedGeneration [ a prov:Generation,
                prov:Influence,
                prov:InstantaneousEvent ;
            prov:activity <ex:compose1> ;
            prov:hadRole <ex:composedData> ;
            prov:influencer <ex:compose1> ] ;
    prov:wasGeneratedBy <ex:compose1> ;
    prov:wasInfluencedBy <ex:compose1> .

<ex:edith> a prov:Agent,
        prov:Person ;
    prov:influenced <ex:correct1> .

<ex:illustrate1> a prov:Activity ;
    prov:generated <ex:chart1> ;
    prov:influenced <ex:chart1> ;
    prov:used <ex:composition1> ;
    prov:wasAssociatedWith <ex:derek> ;
    prov:wasInfluencedBy <ex:composition1>,
        <ex:derek> .

<ex:regionList> a prov:Entity ;
    prov:influenced <ex:compose1> .

<ex:dataset2> a prov:Entity ;
    prov:influenced <ex:chart2> ;
    prov:wasDerivedFrom <ex:dataset1> ;
    prov:wasGeneratedBy <ex:correct1> ;
    prov:wasInfluencedBy <ex:correct1>,
        <ex:dataset1> ;
    prov:wasRevisionOf <ex:dataset1> .

<ex:chart1> a prov:Entity ;
    prov:generatedAtTime "2012-03-02T10:30:00"^^xsd:dateTime ;
    prov:influenced <ex:chart2> ;
    prov:wasAttributedTo <ex:derek> ;
    prov:wasGeneratedBy <ex:illustrate1> ;
    prov:wasInfluencedBy <ex:derek>,
        <ex:illustrate1> .

<ex:article> a prov:Entity ;
    dct:title "Crime rises in cities" ;
    prov:alternateOf <ex:article_v1>,
        <ex:article_v2> ;
    prov:influenced <ex:quoteInBlogEntry-20130326> .

<ex:compose1> a prov:Activity ;
    prov:generated <ex:composition1> ;
    prov:influenced <ex:composition1> ;
    prov:qualifiedAssociation [ a prov:Association,
                prov:Influence ;
            prov:agent <ex:derek> ;
            prov:hadRole <ex:analyst> ;
            prov:influencer <ex:derek> ] ;
    prov:qualifiedUsage [ a prov:Influence,
                prov:InstantaneousEvent,
                prov:Usage ;
            prov:entity <ex:dataset1> ;
            prov:hadRole <ex:dataToCompose> ;
            prov:influencer <ex:dataset1> ],
        [ a prov:Influence,
                prov:InstantaneousEvent,
                prov:Usage ;
            prov:entity <ex:regionList> ;
            prov:hadRole <ex:regionsToAggregateBy> ;
            prov:influencer <ex:regionList> ] ;
    prov:used <ex:dataset1>,
        <ex:regionList> ;
    prov:wasAssociatedWith <ex:derek> ;
    prov:wasInfluencedBy <ex:dataset1>,
        <ex:derek>,
        <ex:regionList> .

<ex:dataset1> a prov:Entity ;
    prov:influenced <ex:compose1>,
        <ex:dataset2> .

<ex:derek> a prov:Agent,
        prov:Person ;
    prov:actedOnBehalfOf <ex:chartgen> ;
    prov:influenced <ex:chart1>,
        <ex:compose1>,
        <ex:illustrate1> ;
    prov:wasInfluencedBy <ex:chartgen> ;
    foaf:givenName "Derek" ;
    foaf:mbox <mailto:derek@example.org> .
```
