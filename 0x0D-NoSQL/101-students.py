#!/usr/bin/env python3
"This is a line of text"
import pymongo


def top_students(mongo_collection: object):
    "This is a line of text"
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}}
        },
        {"$sort": {"averageScore": -1}}
    ])
