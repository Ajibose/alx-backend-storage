#!/usr/bin/env python3
"""
    Contains a fuction that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
	Lists all document in a collection

        mongo_collection:
            A mongodb collection object

        Returns:
            List of all document in the collection
    """
    if mongo_collection is None:
        return []

    return [doc for doc in mongo_collection.find()]
