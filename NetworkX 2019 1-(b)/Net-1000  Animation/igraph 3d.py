
import igraph as ig

import json
import urllib2

data = []
req = urllib2.Request("miserables.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.loads(f.read())

print (data.keys())
