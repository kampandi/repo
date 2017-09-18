#!/usr/bin/python

count = 0
numbers=raw_input("enter the numbers (ex:93, 90, 67, 58, 45, 45, 13): ")
numbers=numbers.split(',')
numbers=map(int,numbers)
numbers.sort()
numbers.reverse()
x=numbers[0]

for i in numbers:
	count = count + 1
	if i != x and i < x:
		if count == 3:
			print i
			break
