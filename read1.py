import urllib2,json,base64
accesstoken = "GBSR8NESEMWDEA15929E"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10007772.json"
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)
print ("1000772 is "+data['Name'])

url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10003270.json"
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)
print ("10003270 is " + data['Name'])

url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10007800.json"
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)
print ("10007800 is "+ data['Name'])