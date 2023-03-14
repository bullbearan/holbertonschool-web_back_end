#!/usr/bin/env python3
"This is a line of text"
import pymongo


def update_topics(mongo_collection, name, topics):
    "This is a line of text"
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
