#!/usr/bin/python

#numbers=[-2,-4,-7,5,9,10]
numbers=raw_input("Enter the +ve and -ve numbers (ex:-2,-4,-7,5,9,10): ")
numbers=numbers.split(',')
numbers=map(int,numbers)
negative_numbers=0
postitive_numbers=0

for i in numbers:
	if i < 0:
		negative_numbers=negative_numbers + 1
	else:
		postitive_numbers=postitive_numbers + 1
		
print ("total count of negative numbers in the array are: ", negative_numbers)
print ("total count of positive numbers in the array are: ", postitive_numbers)
