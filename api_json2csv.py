#!/usr/bin/python3
import json
import csv
import requests
import urllib3
urllib3.disable_warnings() #bypass SSL, cheap trick

token = '' #place your OAuth-token here
#
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format(token),
    }
response = requests.get('', headers=headers, verify=False) #place your api-url here
#
data = response.json()
headers = ('', '', '') #set some default column names for the 1st row
with open('output.csv', mode='a') as output:
    writeln = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writeln.writerow(headers)

for i in range(len(data)):
    elem = data[i]
    props = elem['properties']
    elemlist = (elem['some_element'], elem['another_element'], props['some_property'][0])
    with open('output.csv', mode='a') as output:
        writeln = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writeln.writerow(elemlist)

output.close()
