__author__ = 'szednik'

from kleio import prov

# load the existing PROV-O graph
prov.graph.load("load-example.ttl", format="turtle")

# get a reference to the existing entity with id="test:entity"
entity = prov.Entity("test:entity")

# define a new entity and say it was derived from "test:entity"
derived_entity = prov.Entity("test:derived_entity")
derived_entity.set_label("derived example entity")
derived_entity.set_was_derived_from(entity)

# print out the updated provenance graph
print(prov.serialize())