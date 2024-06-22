#!/usr/bin/env python3
"""Write a function that provides some stats about a Nginx log collection

prototype: show_stats(collection)
collection is the collection object to use
Display output in this format
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with the number of documents with: method=GET, path=/status
"""


def show_stats(collection, method):
    """show stats about Nginx logs"""
    no_of_docs = collection.count_documents({})
    docs_with_get = collection.count_documents(
            {'method': {"$in": [method[0]]}})
    docs_with_post = collection.count_documents(
            {'method': {"$in": [method[1]]}})
    docs_with_put = collection.count_documents(
            {'method': {"$in": [method[2]]}})
    docs_with_patch = collection.count_documents(
            {'method': {"$in": [method[3]]}})
    docs_with_delete = collection.count_documents(
            {'method': {"$in": [method[4]]}})
    docs_with_get_status = collection.count_documents({
        '$and': [
            {'method': {"$in": [method[0]]}},
            {'path': '/status'}
        ]
    })

    print("{} logs\nMethods:\n"
          "\tmethod GET: {}\n"
          "\tmethod POST: {}\n"
          "\tmethod PUT: {}\n"
          "\tmethod PATCH: {}\n"
          "\tmethod DELETE: {}\n"
          "{} status check".format(
                no_of_docs,
                docs_with_get,
                docs_with_post,
                docs_with_put,
                docs_with_patch,
                docs_with_delete,
                docs_with_get_status
            ))


def show_top_ips(collection):
    """Display top 10 of the most present IPs in the collection"""
    aggregate_query = collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },

        {
            "$sort": {"count": -1}
        },

        {
            "$limit": 10
        }
    ])

    print("IPs:")
    for doc in aggregate_query:
        print("\t{}: {}".format(doc['_id'], doc['count']))


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    show_stats(nginx_collection, ["GET", "POST", "PUT", "PATCH", "DELETE"])
    show_top_ips(nginx_collection)
