import urllib.request
import json
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# arg e.g. https://tor2web.io/ https://onion.to

TOR2WEB_DATA_URL = '/antanistaticmap/stats/yesterday'

req = urllib.request.Request(sys.argv[1] + TOR2WEB_DATA_URL)
with urllib.request.urlopen(req) as res:
    body = json.loads(res.read().decode('utf-8'))

services = body['hidden_services']
services.sort(key=lambda x: x['access_count'])
services.reverse()
for service in services:
    print("URL: {}.onion , Count: {}".format(service['id'], service['access_count']))