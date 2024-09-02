from flask_pymongo import PyMongo
from ..config import Config

mongo = PyMongo()

class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age
