from bs4 import BeautifulSoup
import urllib
import socket
import json
import sys
searchurl = "http://www.evomovies.com/"
# print searchurl
f = urllib.urlopen(searchurl)
html = f.read()
soup = BeautifulSoup(html,"lxml")
# soup = BeautifulSoup("http://cyro.se")
# print "yess"
# print soup.prettify()[0:10000]
# form = soup.find('div', id='footer')
# print len(form.find_all('div', 'footer '))
rating=[]
for link in soup.findAll('div', {'class': 'project-title'}):
	temp=link.find('h2')
	# print temp.text
	if all(ord(char) < 128 for char in temp.text):
		url="http://www.omdbapi.com/?t="+str(temp.text)	
		f1 = urllib.urlopen(url)
		html1 = f1.read()
		soup1 = BeautifulSoup(html1,"lxml")
		temp1=soup1.find("body")
		temp2=temp1.text

		if "Movie not found!" in temp2:
			rating.append("Movie not found!")
		else:
			parsed=json.loads(temp2)
			rating.append(parsed["imdbRating"])
			print parsed["imdbRating"]
	else:
		rating.append("Movie not found!")
print rating
	# # data=
	# jsonData = jsonResponse[temp2]
	# for item in jsonData:
	# 	campaignID = item.get("imdbRating")
	# 	print campaignID
