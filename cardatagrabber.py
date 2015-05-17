import urllib #used to get data from website
import re #for regular expressions

#get the page text


def getAllCarSafetyInfo():

	for i in range(10000):
		id_string = str(i)
		id_string = id_string.zfill(4)		
		print "id: ", id_string
		printInfoById(id_string)	
		
		

def printInfoById(number):
	
	pageInfo = urllib.urlopen("http://www.nhtsa.gov/webapi/api/SafetyRatings/VehicleId/"+number+"?format=json")
	for line in pageInfo:
		print line

	
getAllCarSafetyInfo() 

