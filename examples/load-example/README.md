This example shows a script that loads a provenance trace from load-example.ttl, adds a new entity to the provenance trace, and serializes the modified trace in RDF/XML.

output:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
   xmlns:foaf="http://xmlns.com/foaf/0.1/"
   xmlns:prov="http://www.w3.org/ns/prov#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
>
  <rdf:Description rdf:about="test:bob">
    <foaf:name>Bob</foaf:name>
    <prov:influenced rdf:resource="test:entity"/>
    <prov:influenced rdf:resource="test:activity"/>
    <rdf:type rdf:resource="http://www.w3.org/ns/prov#Person"/>
  </rdf:Description>
  <rdf:Description rdf:about="test:activity">
    <prov:wasInfluencedBy rdf:resource="test:bob"/>
    <rdf:type rdf:resource="http://www.w3.org/ns/prov#Activity"/>
    <prov:generated rdf:resource="test:entity"/>
    <prov:influenced rdf:resource="test:entity"/>
    <rdfs:label>example activity</rdfs:label>
    <prov:wasAssociatedWith rdf:resource="test:bob"/>
  </rdf:Description>
  <rdf:Description rdf:about="test:entity">
    <prov:wasAttributedTo rdf:resource="test:bob"/>
    <prov:wasInfluencedBy rdf:resource="test:bob"/>
    <rdfs:label>example entity</rdfs:label>
    <prov:wasGeneratedBy rdf:resource="test:activity"/>
    <prov:influenced rdf:resource="test:derived_entity"/>
    <rdf:type rdf:resource="http://www.w3.org/ns/prov#Entity"/>
    <prov:wasInfluencedBy rdf:resource="test:activity"/>
  </rdf:Description>
  <rdf:Description rdf:about="test:derived_entity">
    <prov:wasInfluencedBy rdf:resource="test:entity"/>
    <prov:wasDerivedFrom rdf:resource="test:entity"/>
    <rdfs:label>derived example entity</rdfs:label>
    <rdf:type rdf:resource="http://www.w3.org/ns/prov#Entity"/>
  </rdf:Description>
</rdf:RDF>
```