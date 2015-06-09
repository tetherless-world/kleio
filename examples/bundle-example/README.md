serialize command:
```python
print(prov.serialize(format="trig"))
```
output:
```
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix test: <http://test.com/ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<test:bundle> = {
    test:bundle a prov:Bundle,
            prov:Entity .

    <test:entity-in-bundle> a prov:Entity ;
        rdfs:label "entity in bundle" .
}

<ns1:default> = {
    test:bundle a prov:Bundle,
            prov:Entity ;
        rdfs:label "bundle entity" .

    <test:entity-not-in-bundle> a prov:Entity ;
        rdfs:label "entity not in bundle" .
}
```

serialize command:
```python
print(prov.serialize(format="trig", bundle=my_bundle))
```
output:
```
@prefix ns1: <urn:x-rdflib:> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix test: <http://test.com/ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<test:bundle> = {
    test:bundle a prov:Bundle,
            prov:Entity .

    <test:entity-in-bundle> a prov:Entity ;
        rdfs:label "entity in bundle" .
}
```
