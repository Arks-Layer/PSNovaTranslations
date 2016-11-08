#!/usr/bin/python
# coding=utf8
import re
import os
import pprint
import simplejson
import sys

count = 0
invalid_json_files = []
json_files = [f for f in os.listdir('.') if re.match(r'.*\.json', f)]
for files in json_files:
    with open(files) as json_file:
        try:
            djson = simplejson.load(json_file)
            for rmid in djson:
                if ("Text" in djson[rmid] and (djson[rmid]["Text"] != "")):
                    if ("Enabled" not in djson[rmid] or (djson[rmid]["Enabled"] == False)):
                        if (djson[rmid]["Text"] != "Delete" and "DLC Series" not in djson[rmid]["Text"]):
                           print ("%s:%s" % (files, rmid))
                           pprint.pprint(djson[rmid])
                           #count += 1
        except ValueError as e:
            print("%s: %s") % (files, e)
            invalid_json_files.append(files)

count += len(invalid_json_files)
if count != 0:
    sys.exit("=============\nJSON files with issues: %d" % count)
