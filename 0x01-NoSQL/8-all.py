#!/usr/bin/env python3
""" 8-main """
import pymongo


def list_all(mongo_collection):
    """ 8-main """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["my_db"]
    table = db['school']

    return table.find()
