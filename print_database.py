import json
import pymongo
from pymongo import MongoClient


connection_string = 'mongodb://127.0.0.1:27017'
client = MongoClient(connection_string)
db = client.car_database
collection = db.car_collection

print "Records count: " , db.cars.count()
print "Records: ", list(db.cars.find())




