#!/usr/bin/env python3
""" 9-main """

def insert_school(mongo_collection, **kwargs):
    """ 9-main """
    new = mongo_collection.insert_one(kwargs, )
    
    return new.inserted_id