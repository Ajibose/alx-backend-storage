#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


from pymongo.collection import Collection
from typing import List, Dict, Any


def list_all(mongo_collection):
    """Return list of all docs in collection"""
    if not mongo_collection:
        return []

    return [doc for doc in mongo_collection.find()]
