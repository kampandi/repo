#!/usr/bin/python

out_dict={}

import commands
out=commands.getoutput('cat /etc/passwd')
out=out.split('\n')

for i in out:
	out_dict[i.split(':')[0]]={i.split(':')[2]:i.split(':')[6]}


out_dict=out_dict.items()

for x,y in out_dict:
	for x1,y1 in y.items():
		if int(x1) > 100:
			print x,y1
