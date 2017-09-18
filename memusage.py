#!/usr/bin/python

import commands

if int(commands.getoutput('free -m').split('\n').pop(1).split()[3]) < 200:
	print "mem is greater than 80% usage"
else:
	print "mem is less than 80% usage"
