import sys

for i in sys.argv:
	print i

def sayHello():
	"This is a simple function"
	print 'Hello World'

def printMax(a,b):
	if a>b:
		print a, 'is maximum'
	else:
		print b, 'is maximum'

def ChangeValue(a):
	a = 3
	print a

if __name__ == '__main__':
	b = 5
	ChangeValue(b)
	print b
	print sayHello.__doc__
else :
	print "Module function being imported"
