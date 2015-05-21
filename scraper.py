import urllib2
from bs4 import BeautifulSoup
import requests


#jquery?v=HfRSogE7Xh_0X5rNuOPS5q_95fTz0escN_lSv9VUsTU1:1

url = requests.get("http://www.iihs.org/iihs/topics/driver-death-rates/jquery?v=HfRSogE7Xh_0X5rNuOPS5q_95fTz0escN_lSv9VUsTU1:1")
content = url.text
soup = BeautifulSoup(content)

expr = raw_input("Search for: ")

for expr in soup.find_all(expr):
	print expr.text



