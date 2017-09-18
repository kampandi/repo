#!/usr/bin/python

import commands

out=commands.getoutput("df -h")
out=out.split("\n")
out.pop(0)

for i in out:
	out1=i.replace("%", "")
	out2=out1.split()[4]
	out3=out1.split()
	if int(out2) > 20:
		print ("%s filesystem is greater than 20 percentage" %out3[5])
