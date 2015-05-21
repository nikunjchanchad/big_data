import pymongo
from pymongo import MongoClient
connection_string = 'mongodb://127.0.0.1:27017'
client = MongoClient(connection_string)
client.drop_database('car_database')


