#!/usr/bin/python2.7
# Filename: file.py

poem = '''This is a test poem,
Which I'll song praise to PRC.
You know i'm kidding, right?
Yeah, i'm kidding! '''

print 'Writing string poem to poem.txt...'
f = file("poem.txt", "w")
f.write(poem)
f.close
print 'Writing Done.\n'

print 'Reading string from poem.txt...\n'
f = file("poem.txt")
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line
f.close
print '\nReading Done.'
