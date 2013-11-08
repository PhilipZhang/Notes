#!/usr/bin/python2.7
# Filename: pickling.py

import cPickle as p

shoplistfile = 'shoplist.data'	# the name of the file where we'll store our object

shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
