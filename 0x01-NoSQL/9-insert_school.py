#!/usr/bin/env python3
""" 9-insert_school.py """
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    return mongo_collection.insert_one(kwargs).inserted_id

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created:", new_school_id)
