import os
import re
import csv
import pymongo
from pymongo import MongoClient

databaseName    = 'metro_crime'
directory    = 'csvFiles'

client = MongoClient()
db = client[databaseName]

for filename in os.listdir(directory):
    # remove suffix
    name = re.sub('\.csv$', '', filename)
    name = re.sub('\.txt$', '', name)
    print name
    # create collection of file name
    collection = db[name]
    # open file as read only
    with open(os.path.join(directory, filename), 'r') as aFile:
        # read as a dictionary
        reader = csv.DictReader( aFile )
        # add each row to collection
        for row in reader:
            collection.insert(row)
