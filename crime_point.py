import pymongo
from pymongo import MongoClient
connection_string = 'mongodb://127.0.0.1:27017'
client = MongoClient(connection_string)
db = client.metro_crime
collection = db.crime2014
a = []
class point:
    def __init__(self,id,lat,lng):
        self.id = id
        self.lat = lat
        self.lng = lng

for row in collection:
    class_point = point(row[DR NO],row[Location 1][0],row[Location 1][1])
    a.append(class_point)

print a.count()
