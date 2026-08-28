#!/usr/bin/env python3
"""
Module that updates the topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all documents matching name in mongo_collection,
    setting their topics field to the given list of topics.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )