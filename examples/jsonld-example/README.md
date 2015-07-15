This example shows a script that loads a provenance trace from load-example.json, defines a new entity within the provenance trace, and serializes the modified trace as JSON-LD.

output:
```json
{
    "@context": {
        "prov": "http://www.w3.org/ns/prov#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
    },
    "@graph": [
        {
            "@graph": [
                {
                    "@id": "http://tw.rpi.edu/ns/test#activity",
                    "@type": "prov:Activity",
                    "prov:generated": {
                        "@id": "http://tw.rpi.edu/ns/test#entity"
                    },
                    "prov:influenced": {
                        "@id": "http://tw.rpi.edu/ns/test#entity"
                    },
                    "prov:wasAssociatedWith": {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    },
                    "prov:wasInfluencedBy": {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    },
                    "rdfs:label": "example activity"
                },
                {
                    "@id": "http://tw.rpi.edu/ns/test#entity",
                    "@type": "prov:Entity",
                    "prov:wasAttributedTo": {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    },
                    "prov:wasGeneratedBy": {
                        "@id": "http://tw.rpi.edu/ns/test#activity"
                    },
                    "prov:wasInfluencedBy": [
                        {
                            "@id": "http://tw.rpi.edu/ns/test#bob"
                        },
                        {
                            "@id": "http://tw.rpi.edu/ns/test#activity"
                        }
                    ],
                    "rdfs:label": "example entity"
                },
                {
                    "@id": "http://tw.rpi.edu/ns/test#bob",
                    "@type": "prov:Person",
                    "http://xmlns.com/foaf/0.1/name": "Bob",
                    "prov:influenced": [
                        {
                            "@id": "http://tw.rpi.edu/ns/test#activity"
                        },
                        {
                            "@id": "http://tw.rpi.edu/ns/test#entity"
                        }
                    ]
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