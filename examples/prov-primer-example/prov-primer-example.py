__author__ = 'szednik'

"""
This example was taken from http://www.w3.org/TR/prov-primer
"""

from kleio import prov
from rdflib import Namespace
import rdflib
from datetime import datetime

DCT = Namespace("http://purl.org/dc/terms/")
prov.default_graph.bind("dct", DCT)

FOAF = Namespace("http://xmlns.com/foaf/0.1/")
prov.default_graph.bind("foaf", FOAF)

prov.bind_ns("ex", "http://www.example.org#")

# Entities

article = prov.Entity("ex:article")
article.add(DCT.title, rdflib.Literal("Crime rises in cities"))

dataset1 = prov.Entity("ex:dataset1")

regionList = prov.Entity("ex:regionList")

composition1 = prov.Entity("ex:composition1")

chart1 = prov.Entity("ex:chart1")

# Activities

compile1 = prov.Activity("ex:compile1")

compose1 = prov.Activity("ex:compose1")

illustrate1 = prov.Activity("ex:illustrate1")

# Usage and Generation

compose1.set_used(dataset1)
compose1.set_used(regionList)

composition1.set_was_generated_by(compose1)

illustrate1.set_used(composition1)

chart1.set_was_generated_by(illustrate1)

# Agents and Responsibility

derek = prov.Person("ex:derek")
derek.add(FOAF.givenName, rdflib.Literal("Derek"))
derek.add(FOAF.mbox, rdflib.URIRef("mailto:derek@example.org"))

chartgen = prov.Organization("ex:chartgen")
chartgen.add(FOAF.name, rdflib.Literal("Chart Generators Inc"))

compose1.set_was_associated_with(derek)
illustrate1.set_was_associated_with(derek)
chart1.set_was_attributed_to(derek)

derek.set_acted_on_behalf_of(chartgen)

# Roles

dataToCompose = prov.Role("ex:dataToCompose")
regionsToAggregateBy = prov.Role("ex:regionsToAggregateBy")
composedData = prov.Role("ex:composedData")
analyst = prov.Role("ex:analyst")

compose1.usage(entity=dataset1, role=dataToCompose)
compose1.usage(entity=regionList, role=regionsToAggregateBy)
compose1.association(agent=derek, role=analyst)
composition1.generation(activity=compose1, role=composedData)

# Revision and Derivation

dataset2 = prov.Entity("ex:dataset2")
dataset2.set_was_revision_of(dataset1)

chart2 = prov.Entity("ex:chart2")
chart2.set_was_derived_from(dataset2)
chart2.set_was_revision_of(chart1)

# Plans

correct1 = prov.Activity("ex:correct1")
instructions = prov.Plan("ex:instructions")

edith = prov.Person("ex:edith")

correct1.association(agent=edith, plan=instructions)

dataset2.set_was_generated_by(correct1)

# Time

dt1 = datetime.strptime("2012-03-02T10:30:00", "%Y-%m-%dT%H:%M:%S")
chart1.set_generated_at_time(dt1)

dt2 = datetime.strptime("2012-04-01T15:21:00", "%Y-%m-%dT%H:%M:%S")
chart2.set_generated_at_time(dt2)

dt3 = datetime.strptime("2012-03-31T09:21:00", "%Y-%m-%dT%H:%M:%S")
correct1.set_started_at_time(dt3)

dt4 = datetime.strptime("2012-04-01T15:21:00", "%Y-%m-%dT%H:%M:%S")
correct1.set_ended_at_time(dt4)

# Alternate entities and specialization

quoteInBlogEntry = prov.Entity("ex:quoteInBlogEntry-20130326")
quoteInBlogEntry.set_was_quoted_from(article)

article_v1 = prov.Entity("ex:article_v1")
article_v1.set_specialization_of(article)

article_v2 = prov.Entity("ex:article_v2")
article_v2.set_specialization_of(article)

article_v2.set_alternate_of(article_v1)

# print RDF serialization as turtle

print(prov.serialize(format="turtle"))