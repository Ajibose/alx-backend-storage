#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
   """
        Lists all document in a collection

        mongo_collection:
            A mongodb collection object

        Returns:
            List of all document in the collection
    """ 
    if not mongo_collection:
        return []

    return [doc for doc in mongo_collection.find()]
