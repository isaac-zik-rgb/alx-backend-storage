#!/usr/bin/python3
# Write a Python function that lists all documents in a collection:


def list_all(mongo_collection):
    """List all documents in a collection"""
    cursor = mongo_collection.find()

    document = list(cursor)

    return document
