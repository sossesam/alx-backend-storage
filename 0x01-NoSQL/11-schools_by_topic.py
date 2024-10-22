#!/usr/bin/env python3
""" 11-main """

def schools_by_topic(mongo_collection, topic):
    """ 11-main """
    schools = mongo_collection.find({"topics":topic})
    return schools
