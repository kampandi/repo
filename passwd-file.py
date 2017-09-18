#!/usr/bin/python

with open('/tmp/passwd') as out:
	for i in out:
		sp_lines=i.strip().split(':')
		if sp_lines[-1] in '/bin/bash':
			print "userids which has bash shell is: ", sp_lines[0]



#grep -i bash /etc/passwd | awk -F ':' '{print $1}' - Shell Script

#My Idea

#with open('/tmp/passwd') as out:
#	out1=out.read()
#	out1=out.split('\n')
#	for i in out1:
#		if i.split(':')[-1] in '/bin/bash'
#			print "userids which has bash shell is: ", i.split(':')[0]
