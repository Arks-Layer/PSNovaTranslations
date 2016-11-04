#!/usr/bin/python
import re
import os
import simplejson
import sys

invalid_json_files = []
os.chdir(os.getcwd() + "/story")
json_files = [f for f in os.listdir('.') if re.match(r'.*\.json', f)]
for files in json_files:
    with open(files) as json_file:
        try:
            l = []
            l.append('{')
            l.append(json_file.read()[2:-3])
            l.append('}')
            s = ''.join(l)
            simplejson.loads(s)
        except ValueError as e:
            print("%s: %s") % (files, e)
            invalid_json_files.append(files)

count = len(invalid_json_files)
if count != 0:
    sys.exit("=============\nJSON files with issues: %d" % count)
