#!/usr/bin/env python3
"""
    Contains a function that list all the docuemnts in a mongodb collection
"""


from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, any]]:
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
