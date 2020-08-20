#!/bin/bash

# what:
# Sends notification to desktop user, if the battery is low and it's not charging.
# Suggested application: cronjob
# * * * * * XDG_RUNTIME_DIR=/run/user/$(id -u) batteryNotification.sh
# how:
# Extracts information from command 'acpi'
# Checks status of battery by comparing it to given values.
# Sends notification via 'notify-send'

# dependencies:
# acpi
# libnotify-bin on Debian (notify-send)

status=$(acpi | cut -f 3 -d ' ' | rev | cut -c 2- | rev)
discharging="Discharging"

check100=$(acpi | cut -d " " -f 4 | cut -c 3)
if [ "$check100" = "0" ]
then
	current=100
else
	current=$(acpi | cut -d " " -f 4 | cut -c 1-2)
fi

printf "current battery level: %s\n" "$current"
minimal=95

if [ "$current" -lt "$minimal" ] && [ "$status" = "$discharging" ]
then
	# image not supported by i3 but may be by other window managers
	notify-send -i low-battery.png \
	"Battery low



	"
else
	printf "battery is still full enough and/or charging\n"
fi
