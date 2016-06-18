#!/usr/bin/env python3

import subprocess

cmd = ['acpi']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out = p.stdout.read().decode('utf-8').split(' ')

percent_str = out[3][:-1]
number = int(percent_str[0:percent_str.index("%")]) / 100
if number < 0.1:
    battery = "\uf244"
elif number < 0.25:
    battery = "\uf243"
elif number < 0.5:
    battery = "\uf242"
elif number < 0.75:
    battery = "\uf241"
else:
    battery = "\uf240"

discharge = ""
if out[2] != "Discharging,":
    discharge = "  \uf0e7"

print(battery + discharge + "  " + percent_str)
