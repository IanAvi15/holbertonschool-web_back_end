#!/usr/bin/env python3
"""
Module that returns schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of documents in mongo_collection whose
    topics field contains the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))