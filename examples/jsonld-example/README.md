This example shows a script that loads a provenance trace from load-example.json, defines a new entity within the provenance trace, and serializes the modified trace as JSON-LD.

output:
```json
[
    {
        "@graph": [
            {
                "@id": "http://tw.rpi.edu/ns/test#entity",
                "@type": [
                    "http://www.w3.org/ns/prov#Entity"
                ],
                "http://www.w3.org/2000/01/rdf-schema#label": [
                    {
                        "@value": "example entity"
                    }
                ],
                "http://www.w3.org/ns/prov#wasAttributedTo": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    }
                ],
                "http://www.w3.org/ns/prov#wasGeneratedBy": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#activity"
                    }
                ],
                "http://www.w3.org/ns/prov#wasInfluencedBy": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#activity"
                    },
                    {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    }
                ]
            },
            {
                "@id": "http://tw.rpi.edu/ns/test#bob",
                "@type": [
                    "http://www.w3.org/ns/prov#Person"
                ],
                "http://www.w3.org/ns/prov#influenced": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#activity"
                    },
                    {
                        "@id": "http://tw.rpi.edu/ns/test#entity"
                    }
                ],
                "http://xmlns.com/foaf/0.1/name": [
                    {
                        "@value": "Bob"
                    }
                ]
            },
            {
                "@id": "http://tw.rpi.edu/ns/test#activity",
                "@type": [
                    "http://www.w3.org/ns/prov#Activity"
                ],
                "http://www.w3.org/2000/01/rdf-schema#label": [
                    {
                        "@value": "example activity"
                    }
                ],
                "http://www.w3.org/ns/prov#generated": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#entity"
                    }
                ],
                "http://www.w3.org/ns/prov#influenced": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#entity"
                    }
                ],
                "http://www.w3.org/ns/prov#wasAssociatedWith": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    }
                ],
                "http://www.w3.org/ns/prov#wasInfluencedBy": [
                    {
                        "@id": "http://tw.rpi.edu/ns/test#bob"
                    }
                ]
            }
        ]
    },
    {
        "@graph": [
            {
                "@id": "test:derived_entity",
                "@type": [
                    "http://www.w3.org/ns/prov#Entity"
                ],
                "http://www.w3.org/2000/01/rdf-schema#label": [
                    {
                        "@value": "derived example entity"
                    }
                ],
                "http://www.w3.org/ns/prov#wasDerivedFrom": [
                    {
                        "@id": "test:entity"
                    }
                ],
                "http://www.w3.org/ns/prov#wasInfluencedBy": [
                    {
                        "@id": "test:entity"
                    }
                ]
            },
            {
                "@id": "test:entity",
                "@type": [
                    "http://www.w3.org/ns/prov#Entity"
                ],
                "http://www.w3.org/ns/prov#influenced": [
                    {
                        "@id": "test:derived_entity"
                    }
                ]
            }
        ],
        "@id": "urn:x-rdflib:default"
    }
]
```