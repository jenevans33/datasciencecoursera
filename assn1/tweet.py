import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
urllib_data =  json.load(response)

results =  urllib_data[u'results']

for i in range(10):
    print results[i][u'text']


