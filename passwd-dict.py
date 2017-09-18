#!/usr/bin/python

dict_list={}
import commands
out=commands.getoutput("cat /etc/passwd")
out=out.split('\n')

for i in out:
	b=i.split(':')
	dict_list[b[0]]=i[2:]


print dict_list
