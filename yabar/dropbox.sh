#!/usr/bin/env bash

# Get the status from command line applet
DROP_STATUS="$(dropbox-cli status)"

SYNCED="Up to date"
STOPPED="Dropbox isn't running!"

if [ "$DROP_STATUS" == "$STOPPED" ]; then
	echo "Good"
elif [ "$DROP_STATUS" == "$SYNCED" ]; then
	echo "Syncing..."
else
	echo "IDK"
fi
