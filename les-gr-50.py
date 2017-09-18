#!/usr/bin/python

a=50
b=range(100)
for i in b:
	if i == a:
		print i,"is equal to",a
	elif i < a:
		print i,"is lesser than",a
	else:
		print i,"is greater than",a

