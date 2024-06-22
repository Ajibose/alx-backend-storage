#!/usr/bin/env python3
"""Write a function that return the list of school having a specific topic
from a collection

prototype: schools_by_topic(mongo_collection, topic)
mongo_collection is the collection attribute
topic is be the filter condition and it will be an element of the topics field
Returns an empty list if no document found
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    if mongo_collection is None:
        return []

    query = mongo_collection.find({'topics': {'$in': [topic]}})
    return [doc for doc in query]
