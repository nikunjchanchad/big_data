import urllib #used to get data from website
import re #for regular expressions
import json
import pymongo
from pymongo import MongoClient

connection_string = 'mongodb://127.0.0.1:27017'
client = MongoClient(connection_string)
db = client.car_database
collection = db.car_collection

car_id = raw_input("Enter car id ")

def getInfoById(car_id):
	return db.cars.find({u'VehicleId': car_id})


print list(getInfoById(car_id))

