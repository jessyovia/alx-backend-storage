#!/usr/bin/env python3
""" 11-schools_by_topic.py """
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    return list(mongo_collection.find({"topics": topic}))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    for school in schools_by_topic(school_collection, "Python"):
        print(school)
