#!/bin/bash
args=("$@")

for i in $args
do
	temp=$(sed -e 's/^"//' -e 's/"$//' <<<"$i")
	arg=(${temp//:/ })
	xsetwacom --set "HUION Huion Tablet Pad pad" Button ${arg[0]} "key ${arg[1]}"
done
