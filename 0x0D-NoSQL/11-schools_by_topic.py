#!/usr/bin/env python3
"This is a line of text"
import pymongo


def schools_by_topic(mongo_collection, topic):
    "This is a line of text"
    return mongo_collection.find({"topics": topic})
