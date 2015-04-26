import urllib
import json

baseUrl = "https://www.nhtsa.gov/webapi/api/SafetyRatings"
yearUrl = "/modelyear/"
makeUrl = "/make/"
modelUrl = "/model/";
idUrl    = "/VehicleId/"
suffix  = "?format=json"

years = []
yearMakes = set()
models = set()

class YearMake(object):
    """A class that holds jsut the make and year"""
    def __init__(self, year, make):
        self.year = year
        self.make = make

class Model(object):
    """A class that holds year, make, model, and ID"""
    def __init__(self, year, make, model, id):
        self.year = year
        self.make = make
        self.model = model
        self.id = id

    def updateId( self, newId ):
        self.id = newId

    def theModel():
        print self.model


def jsonResponse( url ):
    print url + suffix
    f = urllib.urlopen(url + suffix)
    contents = f.read()
    return contents

def getYears():
    yearsJson = json.loads( jsonResponse( baseUrl ) )
    yearsArray = yearsJson['Results']
    for yearObj in yearsArray:
        years.append( yearObj['ModelYear'] )

def getYearMakes( year ):
    makesJson = json.loads( jsonResponse( baseUrl + yearUrl + year ) )
    makesArray = makesJson['Results']
    for makeObj in makesArray:
        aYearMake = YearMake( makeObj['ModelYear'], makeObj['Make'] )
        yearMakes.add( aYearMake )

def getModels( year, make ):
    modelsJson = json.loads( jsonResponse( baseUrl + yearUrl + year + makeUrl + make ) )
    modelArray = modelsJson['Results']
    for modelObj in modelArray:
        aModel = Model( modelObj['ModelYear'], modelObj['Make'], modelObj['Model'], modelObj['VehicleId'] )
        models.add( aModel )

def addIds( modelSet ):
    for model in modelSet:
        try:
            modelJson = json.loads( jsonResponse( baseUrl + yearUrl + str(model.year) + makeUrl + model.make + modelUrl + urllib.quote(model.model) ) )
            modelArray = modelJson['Results']
            model.updateId( modelArray[0]['VehicleId'] )
        except ValueError:
            print "invalid url param"

def getReport( vecId ):
    reportJson = json.loads( jsonResponse( baseUrl + idUrl + str(vecId) ) )
    print reportJson

# program begins here
count = 0
getYears()
for year in years:
    getYearMakes( str( year ) )

for yearMake in yearMakes:
    if count < 5:
        getModels( str(yearMake.year), yearMake.make )
        count = count + 1

addIds( models )

for model in models:
    getReport( model.id )
