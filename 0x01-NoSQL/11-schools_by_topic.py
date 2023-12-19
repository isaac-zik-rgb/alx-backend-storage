#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic:"""


import pymongo


def def schools_by_topic(mongo_collection, topic):
    """ Where can I learn Python? """
    return list(mongo_collection.find().sort({"topic":topic}))
