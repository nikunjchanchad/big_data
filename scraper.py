import urllib2
import bs4 as BeautifulSoup

url = urllib2.urlopen("https://www.govtrack.us/data/congress/113/votes/2013/s11/data.json")
content = url.read()
soup = BeautifulSoup(content)

print soup
