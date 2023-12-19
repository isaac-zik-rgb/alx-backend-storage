#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert a document in python"""
    for key,value in kwargs.items():
        mongo_collection.insert_many({key: value})

    return mongo_collection.find({}, {_id:true})
