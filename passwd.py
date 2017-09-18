#!/usr/bin/python

import commands
out=commands.getoutput("cat /etc/passwd")
out=out.split("\n")

for i in out:
	id=i.split(":")[2]
	if int(id) > 50:
		print ("%s user's uid is greater than 50" %i.split(":")[0])
