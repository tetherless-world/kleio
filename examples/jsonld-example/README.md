This example shows a script that loads a provenance trace from load-example.json, defines a new entity within the provenance trace, and serializes the modified trace as JSON-LD.

output:
```json
{
  "@context": {
    "foaf": "http://xmlns.com/foaf/0.1/",
    "prov": "http://www.w3.org/ns/prov#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "test": "http://tw.rpi.edu/ns/test#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@graph": [
        {
          "@id": "test:bob",
          "@type": "prov:Person",
          "foaf:name": "Bob",
          "prov:influenced": [
            {
              "@id": "test:entity"
            },
            {
              "@id": "test:activity"
            }
          ]
        },
        {
          "@id": "test:entity",
          "@type": "prov:Entity",
          "prov:wasAttributedTo": {
            "@id": "test:bob"
          },
          "prov:wasGeneratedBy": {
            "@id": "test:activity"
          },
          "prov:wasInfluencedBy": [
            {
              "@id": "test:bob"
            },
            {
              "@id": "test:activity"
            }
          ],
          "rdfs:label": "example entity"
        },
        {
          "@id": "test:activity",
          "@type": "prov:Activity",
          "prov:generated": {
            "@id": "test:entity"
          },
          "prov:influenced": {
            "@id": "test:entity"
          },
          "prov:wasAssociatedWith": {
            "@id": "test:bob"
          },
          "prov:wasInfluencedBy": {
            "@id": "test:bob"
          },
          "rdfs:label": "example activity"
        }
      ]
    },
    {
      "@graph": [
        {
          "@id": "test:derived_entity",
          "@type": "prov:Entity",
          "prov:wasDerivedFrom": {
            "@id": "test:entity"
          },
          "prov:wasInfluencedBy": {
            "@id": "test:entity"
          },
          "rdfs:label": "derived example entity"
        },
        {
          "@id": "test:entity",
          "@type": "prov:Entity",
          "prov:influenced": {
            "@id": "test:derived_entity"
          }
        }
      ],
      "@id": "urn:x-rdflib:default"
    }
  ]
}
```