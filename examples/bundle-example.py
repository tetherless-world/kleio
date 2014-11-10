__author__ = 'szednik'

from kleio import prov

prov.bind_ns("test", "http://test.com/ns#")

bundle = prov.bundle(id="test:bundle")

entity = prov.Entity(id="test:entity-in-bundle", bundle=bundle)
entity.set_label("entity in bundle")

bundle_entity = prov.Bundle(id="test:bundle", bundle=bundle)
bundle_entity.set_label("bundle entity")

entity_not_in_bundle = prov.Entity(id="test:entity-not-in-bundle")
entity_not_in_bundle.set_label("entity not in bundle")

# Serialize using TriG to see the bundle container as a named graph
# and PROV assertions not associated with a bundle in the default graph
print(prov.serialize(format="trig"))

# Serialize using the bundle parameter to see only PROV
# assertions associated with the specified bundle
print(prov.serialize(format="trig", bundle=bundle))