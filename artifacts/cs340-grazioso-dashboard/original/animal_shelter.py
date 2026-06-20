# Original CS 340 CRUD module - credentials redacted for public publication.

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        # Original implementation used fixed connection values and plaintext
        # credentials. The values are redacted here for public publication.
        USER = "[REDACTED_FOR_PUBLIC_PORTFOLIO]"
        PASS = "[REDACTED_FOR_PUBLIC_PORTFOLIO]"
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        self.client = MongoClient("mongodb://%s:%s@%s:%d" % (USER, PASS, HOST, PORT))
        self.database = self.client["%s" % DB]
        self.collection = self.database["%s" % COL]

    def create(self, data):
        if data is None:
            return False
        try:
            self.database.animals.insert_one(data)
            return True
        except Exception:
            return False

    def read(self, query):
        try:
            return list(self.database.animals.find(query))
        except Exception:
            return []
