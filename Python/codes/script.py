#! /usr/bin/python2.7
# Filename: script.py
length = 5
breadth = 2
area = length * breadth
print 'Area is', area

number = 23
running = True
while running:
	guess = int(raw_input('Enter an integer : '))
	if guess == number:
		print 'Congratulations, you guessed it.'
		print "(but you do not win any prizes!)"
		running = False
	elif guess < number:
		print 'No, it is a little higher than that'		# balabala
	else:
		print 'No, it is a little lower than that'
print 'Done'
