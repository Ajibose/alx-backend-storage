#!/usr/bin/env python3
"""Write a fuction that changes all topics of a school document

prototype: update_topics(mongo_collection, name, topics)
mongo_collection will the collection that contains the document to update
name will be the filter condition
topics will be the updated value of topics field
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    if mongo_collection is None:
        return

    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
