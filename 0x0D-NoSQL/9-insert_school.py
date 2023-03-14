#!/usr/bin/env python3
"This is a line of text"
import pymongo


def insert_school(mongo_collection, **kwargs):
    "This is a line of text"
    return mongo_collection.insert_one(kwargs).inserted_id
