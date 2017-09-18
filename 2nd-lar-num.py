#!/usr/bin/python
#numbers=[45,45,13,58,90,67,93]

import random
numbers=raw_input("enter the numbers with comma (ex:45,45,13,58,90,67,93): ")
numbers=numbers.split(',')
numbers=map(int,numbers)
#random.shuffle(numbers)
numbers.sort()
numbers.reverse()
x=numbers[0]

#print x
#print numbers

for i in numbers:
	if i != x and i < x:
		print i
		break
