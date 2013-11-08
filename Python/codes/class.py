#!/usr/bin/python2.7
# Filename: class.py
class MyClass:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print "Hello, dear", self.name
m = MyClass('Zhang Dejia')
m.sayHi()
