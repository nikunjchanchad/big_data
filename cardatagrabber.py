import urllib #used to get data from website
import re #for regular expressions
import json
import pymongo
from pymongo import MongoClient
connection_string = 'mongodb://127.0.0.1:27017'
client = MongoClient(connection_string)
db = client.car_database
collection = db.car_collection

#get the page text


def getAllCarSafetyInfo():

	for i in range(10000):
		id_string = str(i)
		id_string = id_string.zfill(4)		
		print "Storing car id: ", id_string
		storeInfoById(id_string)	
		
		

def storeInfoById(number):
	
	pageInfo = urllib.urlopen("http://www.nhtsa.gov/webapi/api/SafetyRatings/VehicleId/"+number+"?format=json")
	dct = json.load(pageInfo)
	db.cars.insert(dct)

	
getAllCarSafetyInfo() 




