shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist), 'items to purchase.'
print 'These items are:',
for item in shoplist:
	print item,
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
print 'Item 2 to end is', shoplist[2:]
momlist = ['shampoo', 'soap']
print 'My mom wants to buy', momlist
newlist = [shoplist, momlist]
print 'So, we want to buy', newlist

print '*************************************'
zoo = ('wolf', 'tiger', 'penguin')
print 'Number of animals in the zoo is', len(zoo)
new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in the new zoo are', new_zoo
print 'Animals bought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]

print '*************************************'
ab = { 'Zhang Dejia'	: 'zhang.dejia@gmail.com',
		'Li Mengxiu'	: 'li.mengxiu@gmail.com',
		'Xiu Junjie'	: 'xiu.junjie@gmail.com'}
print "Zhang Dejia's address is %s" % ab['Zhang Dejia']
ab['Xu Qiang'] = 'xu.qiang@gmail.com'
print ab
del ab['Li Mengxiu']
print 'There are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
	print 'Contact %s at %s' % (name, address)
print ab.items()

name = 'Zhangdejia'
print 'characters 1 to 3 is', name[1:3]
print 'characters start to end is', name[:]
print 'characters 1 to -1 is', name[1:-1]


