shoplist = ['apple', 'banana', 'carrot', 'mango']
mylist = shoplist
del mylist[0]
print shoplist
mylist = shoplist[:]
del mylist[0]
print shoplist
print mylist
