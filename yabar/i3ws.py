#!/usr/bin/env python3

import subprocess
import json

command = ['i3-msg', '-t', 'get_workspaces']
p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.stdout.read().decode('utf-8')

pjson = json.loads(text)

acnum = 0
string = ""

for objects in pjson:
    if objects["visible"] == True:
        acnum = objects["name"]

for objects in pjson:
    string += str(objects["name"])
    string += " "

print(string)
