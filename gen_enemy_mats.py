#!/usr/bin/env python3
##-----------------------------------------------------------------------------
##
## Copyright (C) 2016 Arks-Layer, Graham Sanderson
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to
## deal in the Software without restriction, including without limitation the
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
## sell copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
## IN THE SOFTWARE.
##
##-----------------------------------------------------------------------------
##
## Generates some easy translations relating to enemies.
##
##-----------------------------------------------------------------------------

import json
import re
import sys


## Function Definitions ------------------------------------------------------|

##
## LoadEnemies
##
def LoadEnemies(fname):
#{
   ret = {
      "ダーカー": "Darker",
      "獣":       "Monster",
      "巨大獣":   "Giant Monster",
      "鳥":       "Bird"
   }

   j = json.load(open(fname, "r"))

   for code in j:
   #{
      obj = j[code]

      if "Text" in obj and "Enabled" in obj and obj["Enabled"]:
         ret[obj["OriginalText"]] = obj["Text"]
   #}

   return ret
#}

##
## Item
##
def Item(items, name):
#{
   item = items[name]
   if type(item) is list: return item[0]
   else:                  return item
#}

##
## UpToDateItem
##
def UpToDateItem(ln, item):
#{
   if type(item) is list:
   #{
      for k in item:
         if ln.find(k) != -1:
            return True
      return False
   #}
   else:
      return ln.find(item) != -1
#}

##
## ProcFile
##
def ProcFile(fp, out, enemies, items, delimiters):
#{
   for ln in fp:
   #{
      for delim in delimiters:
      #{
         match = re.match("\\s+\"OriginalText\": \"(.+)" + delim + "(.+)\",\n", ln)

         if match is not None and         \
            match.group(1) in enemies and \
            match.group(2) in items:
         #{
            ln1 = next(fp)

            name = enemies[match.group(1)]
            item = Item(items, match.group(2))

            if not UpToDateItem(ln1, items[match.group(2)]):
            #{
               ln = ln + \
                    "    \"Text\": \"" + name + " " + item + "\",\n" + \
                    "    \"Enabled\": true\r\n"

               ln2 = next(fp)
               if ln2.find("\"Enabled\"") == -1: ln = ln + ln2
            #}
            else:
               ln = ln + ln1
            
            break
         #}
      #}
      
      out.write(ln)
   #}
#}

##
## Main
##
def Main():
#{
   enemies = LoadEnemies("rmd/Enemies.json")

   with open("rmd/Materials.json", "r", newline = "") as fp:
      with open("rmd/Materials.json.1", "w", newline = "") as out:
         ProcFile(fp, out, enemies,
         {
            "甲殻":   "Shell",
            "目片":   "Eye Piece",
            "眼片":   "Eyeball",
            "刃片":   "Blade",
            "脚片":   "Leg",
            "鱗片":   "Scale",
            "殻片":   "Husk Part",
            "殻":     "Husk",
            "皮片":   "Pelt",
            "爪片":   "Claw Part",
            "爪":     "Claw",
            "ヒレ片": "Fillet",
            "羽片":   "Wing",
            "針片":   "Stinger",
            "牙片":   "Fang",
            "盾片":   "Exoskeleton",
            "骨":     "Bone",
            "肉":     [ "Flesh", "Meat" ],
            "ミルク": "Milk"
         }, ["の"])

   with open("rmd/Enemy Cores.json", "r", newline = "") as fp:
      with open("rmd/Enemy Cores.json.1", "w", newline = "") as out:
         ProcFile(fp, out, enemies,
         {
            "コア":   "Core",
            "超コア": "Super Core",
            "極コア": "Climax Core"
         }, ["の", "・"])
#}


## Entry Point ---------------------------------------------------------------|

if __name__ == "__main__": Main()

## EOF
