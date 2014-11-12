Kleio
=====

[![Build Status](https://travis-ci.org/tetherless-world/kleio.svg?branch=master)](https://travis-ci.org/tetherless-world/kleio) [![License](http://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/tetherless-world/kleio/blob/master/LICENSE) [![Latest Release](https://badge.fury.io/py/kleio.svg)](http://badge.fury.io/py/kleio) [![Downloads](https://pypip.in/download/kleio/badge.svg)](https://pypi.python.org/pypi/kleio/)

A python library for W3C Provenance Data Model supporting PROV-O.

Kleio is free software released under the MIT license.

Features
--------

* An implementation of the W3C PROV Data Model in Python
* Supports serialization and deserialization as PROV-O in RDF/XML, Turtle, TriG, N3, NTriples, and JSON-LD formats
* Supports provenance-of-provenance (PROV bundles) via named graphs
* Built using [RDFlib](https://github.com/RDFLib/rdflib)

Getting Started
---------------

Kleio can be installed from PyPI using the pip installer:

    $ pip install kleio

From kleio use the prov module to generate PROV records and output PROV-O.

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

Kleio can also be used to load and update existing PROV-O records.

```python

from kleio import prov

# load the existing PROV-O graph
prov.graph.load("load-example.ttl", format="turtle")

# get a reference to the existing entity with id="test:entity"
entity = prov.Entity("test:entity")

# ... update entity ...
```

Support
-------

More information is available on the project webpage:

https://github.com/tetherless-world/kleio

Continuous integration status details available from Travis CI:

https://travis-ci.org/tetherless-world/kleio

The documentation can be built by doing:

    $ python setup.py build_sphinx

And is also available from ReadTheDocs:

http://kleio.readthedocs.org/en/latest