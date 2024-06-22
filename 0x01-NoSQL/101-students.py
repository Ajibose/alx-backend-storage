"""Write a function that returns all document sorted bt their average score

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore
"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    if mongo_collection is None:
        return []

    res = mongo_collection.aggregate([
        {
            "$unwind": "$topics"
        },

        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },

        {
            "$sort": {"averageScore": -1}
        }

    ])

    return [doc for doc in res]
