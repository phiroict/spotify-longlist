__author__ = 'phiro'

import http.client
import Constants
import json

class APITest:
    keys = {}

    def readKeys(self):
        with open("../licensekeys.properties") as reader:
            for line in reader:
                line = line.rstrip() #removes trailing whitespace and '\n' chars

                if "=" not in line: continue #skips blanks and comments w/o =
                if line.startswith("#"): continue #skips comments which contain =

                k, v = line.split("=", 1)
                self.keys[k] = v

    def searchArtist(self,query="weezer"):
        h = http.client.HTTPSConnection(Constants.base_url)
        request = Constants.search_url.format("weezer&type=artist")
        print("Calling {}".format(request))
        h.request("GET", request)
        r = h.getresponse()

        obj = json.loads(r.read().decode('utf-8'))
        print(str(obj["artists"]["offset"]))

def searchZeroPopulair(self,query="weezer"):
    h = http.client.HTTPSConnection(Constants.base_url)
    request = Constants.search_url.format("weezer&type=artist")
    print("Calling {}".format(request))
    h.request("GET", request)
    r = h.getresponse()

    obj = json.loads(r.read().decode('utf-8'))
    print(str(obj["artists"]["offset"]))



# Test entry
a = APITest()
a.readKeys()
a.searchArtist()
