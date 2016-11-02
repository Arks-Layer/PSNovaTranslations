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
   ret = \
   {
      "ダーカー": "Darker",
      "獣":       "Monster",
      "巨大獣":   "Giant Monster",
      "鳥":       "Bird"
   }

   j   = json.loads("{" + open(fname, "r").read()[:-2] + "}")

   for code in j:
   #{
      obj = j[code]
      if "Text" in obj and "Enabled" in obj:
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
   for k in item:
      if ln.find(k) != -1:
         return True

   return False
#}

##
## UpToDate
##
def UpToDate(ln, name, item):
#{
   if ln.find("\"Enabled\"") != -1 or \
      ln.find(name) == -1 or \
      not UpToDateItem(ln, item):
      return False

   return True
#}

##
## ProcFile
##
def ProcFile(fp, out, enemies, items):
#{
   for ln in fp:
   #{
      match = re.match("\\s+\"OriginalText\": \"(.+)の(.+)\",\r\n", ln)

      if match is not None and         \
         match.group(1) in enemies and \
         match.group(2) in items:
      #{
         ln1 = next(fp)

         name = enemies[match.group(1)]
         item = Item(items, match.group(2))

         if not UpToDate(ln1, name, items[match.group(2)]):
         #{
            ln = ln + \
                 "    \"Text\": \"" + name + " " + item + "\",\r\n" + \
                 "    \"Enabled\": true\r\n"

            ln2 = next(fp)
            if ln2.find("\"Enabled\"") == -1: ln = ln + ln2
         #}
         else:
            ln = ln + ln1
      #}

      out.write(ln)
   #}
#}

##
## Main
##
def Main():
#{
   enemies = LoadEnemies("enemies.json")

   with open("misc_items.json", "r", newline = "") as fp:
      with open("misc_items.json.1", "w", newline = "") as out:
         ProcFile(fp, out, enemies,
         {
            "甲殻":   "Shell",
            "目片":   "Eye",
            "眼片":   "Eye",
            "刃片":   "Blade",
            "脚片":   "Leg",
            "鱗片":   "Scale",
            "殻片":   "Husk",
            "殻":     "Husk",
            "皮片":   "Pelt",
            "爪片":   "Claw",
            "爪":     "Claw",
            "ヒレ片": "Fillet",
            "羽片":   "Wing",
            "針片":   "Stinger",
            "牙片":   "Fang",
            "盾片":   "Exoskeleton",
            "骨":     "Bone",
            "肉":     [ "Flesh", "Meat" ],
            "ミルク": "Milk"
         })

   with open("enemy_cores.json", "r", newline = "") as fp:
      with open("enemy_cores.json.1", "w", newline = "") as out:
         ProcFile(fp, out, enemies, { "・コア": "Core" })
#}


## Entry Point ---------------------------------------------------------------|

if __name__ == "__main__": Main()

## EOF
