#!/usr/bin/python

class Calc():
	def __init__(self, x, y):
		self.x=x
		self.y=y
	def addition(self):
		return(self.x + self.y)
	def subtraction(self):
		return(self.x - self.y)
	def multiplication(self):
		return(self.x * self.y)
	def devision(self):
		return(self.x / self.y)
	def modulus(self):
		return(self.x % self.y)
	def exponent(self):
		return(self.x ** self.y)
	def floor_division(self):
		return(self.x // self.y)
