#!/usr/bin/env python3
""" 8-main """
import pymongo


def list_all(mongo_collection):
    """ 8-main """
    all_schools = mongo_collection.find()
    return all_schools
