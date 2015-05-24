import pymongo
import re
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

for row in collection.find():
    if row["Location 1"]:
        b = []
        str = row["Location 1"]
        loc = re.sub(r'[()\s]',"",str)
        b = loc.split(',')
        class_point = point(row["DR NO"],b[0],b[1])
        a.append(class_point)

print a.count()
