#!/usr/bin/python

con_dict={}
#j=0

with open('/tmp/word_count.txt') as out:
	for i in out.read().split():
		if i in con_dict:
			con_dict[i] += 1
		else:
			con_dict[i]=1


print (con_dict)
