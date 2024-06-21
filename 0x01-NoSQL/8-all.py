#!/usr/bin/env python3
"""
    A module that contains s function that Lists all documents in a collection
"""
from typing import List, Any, Dict
from pymongo import MongoClient
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
        Lists all document in a collection

        mongo_collection:
            A mongodb collection object

        Returns:
            List of all document in the collection
    """
    doc_list = [doc for doc in mongo_collection.find()]
    return doc_list
