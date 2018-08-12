#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
from collections import OrderedDict
import fnmatch
import json
import os
import re
import sys

# error counter
counterr = 0

if (sys.version_info >= (3, 2)):
    indent = "\t"
else:
    indent = 4

separators = (',', ': ')


# Need the json path
if len(sys.argv) < 2:
    dir = "rmd"
else:
    dir = sys.argv[1]

# collect all the JSON files
json_files = [
    os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(dir)
    for f in fnmatch.filter(files, '*.json')
]

for files in json_files:
    update = False
    with codecs.open(files, mode='r', encoding='utf-8') as json_file:
        sfile = json_file.read()
        sjson = json.loads(sfile, object_pairs_hook=OrderedDict)
        djson = json.dumps(sjson, ensure_ascii=False, indent=2, separators=separators)
        if (indent == 4):
            djson = re.sub('\n +', lambda match: '\n' + '\t' * (len(match.group().strip('\n')) / 4), djson)
        djson += "\n"
        if (sfile != djson):
            update = True

    if (update):
        counterr += 1
        print("Tidy up {}".format(files))
        with codecs.open(files, mode='w+', encoding='utf-8') as json_file:
            json_file.write(djson)
        counterr += 1

if counterr > 0:
    sys.exit("Issues found")
