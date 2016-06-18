#!/usr/bin/env bash

NAME=`iwconfig wlp6s0 | grep ESSID | awk '{print $4}' | tr -d 'ESID:"'`

if [ "$NAME" == "off/any" ]; then
	echo "WIFI OFF"
else
	echo "WIFI: " $NAME
fi
