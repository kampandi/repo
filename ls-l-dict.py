#!/usr/bin/python

dict_list={}
import commands
out=commands.getoutput("ls -l /root/practice")
out=out.split('\n')
out.pop(0)

for i in out:
	a=i.split()
	dict_list[a[8]]=a[:-1]


print dict_list
