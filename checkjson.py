#!/usr/bin/python
# coding=utf8
import re
import os
import pprint
import simplejson
import sys

counterr = 0
invalid_json_files = []
os.chdir(os.getcwd() + "/rmd")
json_files = [f for f in os.listdir('.') if re.match(r'.*\.json', f)]
for files in json_files:
    with open(files) as json_file:
        try:
            countin = 0
            countout = 0
            djson = simplejson.load(json_file)
            for rmid in djson:
                countin += 1
                if ("Text" in djson[rmid] and (djson[rmid]["Text"] != "")):
                    if ("Enabled" not in djson[rmid] or (djson[rmid]["Enabled"] == False)):
                       print ("%s:%s entry not enabled" % (files, rmid))
                       pprint.pprint(djson[rmid])
                       #counterr += 1
                    if ("[" in djson[rmid]["Text"]) and not ("]" in djson[rmid]["Text"]):
                       print ("%s:%s unclosed [" % (files, rmid))
                       pprint.pprint(djson[rmid])
                       counterr += 1
                    if ("]" in djson[rmid]["Text"]) and not ("[" in djson[rmid]["Text"]):
                       print ("%s:%s unclosed ]" % (files, rmid))
                       pprint.pprint(djson[rmid])
                       counterr += 1
        except ValueError as e:
            print("%s: %s") % (files, e)
            invalid_json_files.append(files)

counterr += len(invalid_json_files)
if counterr != 0:
    sys.exit("=============\nJSON files with issues: %d" % counterr)
