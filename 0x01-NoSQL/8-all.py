#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""
from typing import List, Any, Dict
from pymongo import MongoClient
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """Return list of all docs in collection"""
    doc_list = [doc for doc in mongo_collection.find()]
    return doc_list
