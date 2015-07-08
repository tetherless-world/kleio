__author__ = 'szednik'

import unittest
from datetime import datetime
from rdflib.resource import Resource
from rdflib import Graph
from rdflib.plugin import PluginException

from kleio import prov


class TestPROV(unittest.TestCase):

    def setUp(self):
        prov.clear_graph()
        prov.ns("test", "http://tw.rpi.edu/ns/test#")

    def get_datetime(self, dt):
        return datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")

    def test_entity_constructor(self):
        entity = prov.Entity("test:entity")
        self.assertEqual(entity.identifier, entity.identifier)

    def test_entity_bnode(self):
        entity = prov.Entity()
        self.assertTrue(isinstance(entity, prov.Entity))

    def test_entity_label(self):
        entity = prov.Entity("test:entity")
        entity.set_label("test label")
        self.assertEqual(entity.get_label()[0], "test label")

    def test_entity_no_label(self):
        entity = prov.Entity("test:entity")
        self.assertEqual(entity.get_label(), [])

    def test_collection_constructor(self):
        collection = prov.Collection("test:collection")
        self.assertEqual(collection.identifier, collection.identifier)

    def test_collection_bnode(self):
        collection = prov.Collection()
        self.assertTrue(isinstance(collection, Resource))

    def test_collection_isinstance_of_entity(self):
        collection = prov.Collection("test:collection")
        self.assertTrue(isinstance(collection, prov.Entity))

    def test_activity_constructor(self):
        activity = prov.Activity("test:activity")
        self.assertEqual(activity.identifier, activity.identifier)

    def test_agent_constructor(self):
        agent = prov.Agent("test:agent")
        self.assertEqual(agent.identifier, agent.identifier)

    def test_location_constructor(self):
        location = prov.Location("test:location")
        self.assertEqual(location.identifier, location.identifier)

    def test_role_constructor(self):
        role = prov.Role("test:role")
        self.assertTrue(isinstance(role, Resource))
        self.assertEqual(role.identifier, role.identifier)

    def test_role_bnode(self):
        role = prov.Role()
        self.assertTrue(isinstance(role, prov.Role))

    def test_usage_bnode(self):
        usage = prov.Usage()
        self.assertIsNotNone(usage)

    def test_instantaneous_event_bnode(self):
        event = prov.InstantaneousEvent()
        self.assertIsNotNone(event)

    def test_influence_bnode(self):
        influence = prov.Influence()
        self.assertIsNotNone(influence)

    def test_usage(self):
        activity = prov.Activity("test:activity")
        role = prov.Role("test:role")
        entity = prov.Entity("test:entity")
        usage = activity.usage(entity, role=role)
        self.assertTrue(isinstance(usage, prov.Usage))

    def test_generation(self):
        entity = prov.Entity("test:entity")
        activity = prov.Activity("test:activity")
        generation = entity.generation(activity)
        self.assertTrue(isinstance(generation, prov.Generation))

    def test_derivation(self):
        e1 = prov.Entity("test:e1")
        e2 = prov.Entity("test:e2")
        derivation = e2.derivation(e1)
        self.assertTrue(isinstance(derivation, prov.Derivation))

    def test_attribution(self):
        entity = prov.Entity("test:entity")
        agent = prov.Agent("test:agent")
        attribution = entity.attribution(agent)
        self.assertTrue(isinstance(attribution, prov.Attribution))

    def test_get_used(self):
        entity = prov.Entity("test:e1")
        activity = prov.Activity("test:activity")
        activity.set_used(entity)
        used_entity = activity.get_used()
        self.assertEqual(used_entity[0].identifier, entity.identifier)

    def test_many_get_used(self):
        e1 = prov.Entity("test:e1")
        e2 = prov.Entity("test:e2")
        activity = prov.Activity("test:activity")
        activity.set_used(e1)
        activity.set_used(e2)
        used_entities = activity.get_used()
        used_entities = sorted(used_entities, key=lambda entity: entity.identifier)
        self.assertEqual(len(used_entities), 2)
        self.assertEqual(used_entities[0].identifier, e1.identifier)
        self.assertEqual(used_entities[1].identifier, e2.identifier)

    def test_get_was_generated_by(self):
        entity = prov.Entity("test:e1")
        activity = prov.Activity("test:activity")
        entity.set_was_generated_by(activity)
        generated_by = entity.get_was_generated_by()
        self.assertEqual(generated_by[0].identifier, activity.identifier)

    def test_get_was_attributed_to(self):
        entity = prov.Entity("test:e1")
        agent = prov.Agent("test:agent")
        entity.set_was_attributed_to(agent)
        attributed_to = entity.get_was_attributed_to()
        self.assertEqual(attributed_to[0].identifier, agent.identifier)

    def test_get_had_primary_source(self):
        e1 = prov.Entity("test:e1")
        e2 = prov.Entity("test:e2")
        e2.set_had_primary_source(e1)
        primary_sources = e2.get_had_primary_source()
        self.assertEqual(primary_sources[0].identifier, e1.identifier)

    def test_get_generated_at_time(self):
        e1 = prov.Entity("test:e1")
        dt_str = "2014-05-01T00:00:00"
        e1.set_generated_at_time(self.get_datetime(dt_str))
        dt = e1.get_generated_at_time()
        self.assertEqual(dt.isoformat(), dt_str)

    def test_get_started_at_time(self):
        activity = prov.Activity("test:activity")
        dt_str = "2014-05-01T00:00:00"
        activity.set_started_at_time(self.get_datetime(dt_str))
        dt = activity.get_started_at_time()
        self.assertEqual(dt.isoformat(), dt_str)

    def test_get_ended_at_time(self):
        activity = prov.Activity("test:activity")
        dt_str = "2014-05-01T00:00:00"
        activity.set_ended_at_time(self.get_datetime(dt_str))
        dt = activity.get_ended_at_time()
        self.assertEqual(dt.isoformat(), dt_str)

    def test_fully_qualified_derivation(self):
        e1 = prov.Entity("test:e1")
        e2 = prov.Entity("test:e2")
        activity = prov.Activity("test:activity")
        derivation = e2.derivation(e1, id="test:derivation")
        generation = e2.generation(activity, id="test:generation")
        usage = activity.usage(e1, id="test:usage")

        derivation.set_had_generation(generation)
        derivation.set_had_activity(activity)
        derivation.set_had_usage(usage)

        self.assertTrue(isinstance(derivation, prov.Derivation))
        self.assertTrue(isinstance(generation, prov.Generation))
        self.assertTrue(isinstance(usage, prov.Usage))

    def test_urn_entity(self):
        e1 = prov.Entity("urn:hdl:11121/8375-3759-1904-3620-CC")
        self.assertTrue(isinstance(e1, prov.Entity))

    def test_set_was_generated_by(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        activity = prov.Activity("test:activity")
        activity.set_label("example activity")
        entity.set_was_generated_by(activity)
        ttl = prov.serialize(format="turtle")
        self.assertIsNotNone(ttl)

    def test_serialize_default(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        out = prov.serialize()
        self.assertIsNotNone(out)

    def test_serialize_turtle(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        ttl = prov.serialize(format="turtle")
        self.assertIsNotNone(ttl)

    def test_serialize_trig(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        trig = prov.serialize(format="trig")
        self.assertIsNotNone(trig)

    def test_serialize_unknown(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        self.assertRaises(PluginException, prov.serialize, format="unknown")

    def test_serialize_rdfxml(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        rdfxml = prov.serialize(format="xml")
        self.assertIsNotNone(rdfxml)

    def test_serialize_jsonld(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        jsonld = prov.serialize(format="json-ld")
        self.assertIsNotNone(jsonld)

    def test_serialize_n3(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        n3 = prov.serialize(format="n3")
        self.assertIsNotNone(n3)

    def test_serialize_ntriples(self):
        entity = prov.Entity("test:entity")
        entity.set_label("example entity")
        ntriples = prov.serialize(format="nt")
        self.assertIsNotNone(ntriples)

    def test_bundle_factory_method(self):
        bundle = prov.bundle(id="test:bundle")
        self.assertIsNotNone(bundle)
        self.assertTrue(isinstance(bundle, Graph))

    def test_bundled_entity(self):
        bundle = prov.bundle(id="test:bundle")
        e1 = prov.Entity(id="test:entity-in-bundle", bundle=bundle)
        e2 = prov.Entity(id="test:entity-not-in-bundle")
        self.assertTrue(e1.identifier in bundle.subjects())
        self.assertFalse(e2.identifier in bundle.subjects())

    def test_get_bundle_entity(self):
        bundle = prov.bundle(id="test:bundle")
        bundle_entity = prov.bundle_entity(bundle=bundle)
        self.assertIsNotNone(bundle_entity)
        self.assertEqual(bundle.identifier, bundle_entity.identifier)

if __name__ == '__main__':
    unittest.main()