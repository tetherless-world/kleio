Kleio
=====

A python library for W3C Provenance Data Model supporting PROV-O

Getting Started
---------------

Kleio aims to be a pythonic PROV API with support for PROV-O serialization as RDF/XML, N3, Turtle, and JSON-LD.

```python
from kleio import prov

prov.bind_ns("test", "http://tw.rpi.edu/ns/test#")

entity = prov.Entity("test:entity")
entity.set_label("example entity")

activity = prov.Activity("test:activity")
activity.set_label("example activity")

entity.set_was_generated_by(activity)
print(prov.serialize(format="turtle"))
```
output:

```
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix test: <http://tw.rpi.edu/ns/test#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<test:activity> a prov:Activity ;
    rdfs:label "example activity" ;
    prov:generated <test:entity> ;
    prov:influenced <test:entity> .

<test:entity> a prov:Entity ;
    rdfs:label "example entity" ;
    prov:wasGeneratedBy <test:activity> ;
    prov:wasInfluencedBy <test:activity> .
```

Features
--------

...

Support
-------

More information is available on the project webpage:

https://github.com/tetherless-world/kleio

Continuous integration status details available from travis.ci:

[![Build Status](https://travis-ci.org/tetherless-world/kleio.svg?branch=master)](https://travis-ci.org/tetherless-world/kleio)

The documentation can be built by doing::

    $ python setup.py build_sphinx

And is also available from ReadTheDocs:

http://kleio.readthedocs.org/en/latest