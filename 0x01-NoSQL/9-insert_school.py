#!/usr/bin/env python3
"""Write a function that inserts a new document in a collection
The fields of the document will be based on the kwargs provided as an argument
Return the inserted document _id or empty string if not notmongo_collection
prototype: def insert_school(mongo_collection, **kwargs)
mongo_collection will be a collection object to insert the document
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    if mongo_collection is None:
        return ""

    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
