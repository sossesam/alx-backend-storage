#!/usr/bin/env python3
""" 10-main """


def update_topics(mongo_collection, name, topics):
    """ 10-main """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
