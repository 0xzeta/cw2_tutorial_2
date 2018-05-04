import urllib2,json,base64
accesstoken = "GBSR8NESEMWDEA15929E"
institution="10007772"
course="U56119"
page=0
url="http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
	institution,
	course
	)
request = urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic " + base64.encodestring(accesstoken+":").replace('\n','')
    )
response = urllib2.urlopen(request)
data = json.load(response)

for c in data:
	if c['Code'] == 'SALARY':
		d = c['Details']
		for a in d:
			if a ['Code'] == "LDMED":
				print "1.The median salary 6 months after graduation for Software Engineering students from Napier is " + str(a['Value'])



for c in data:
	if c['Code'] == 'SALARY':
		d = c['Details']
		for a in d:
			if a ['Code'] == "INSTMED":
				print "2.The median salary in the sector for software engineering graduates 40 months after gradiuation is " + str(a['Value'])

for c in data:
	if c['Code'] == 'NSS':
		d = c['Details']
		for a in d:
			if a ['Code'] == "Q1":
				print "3.The proportion of software engineering students who agree or strongly agree with the statement [Staff are good at explaining things] is " + str(a['Value'])

