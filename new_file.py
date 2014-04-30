#!/usr/bin/env python


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print animals.index("duck")
animals.insert (2,"cobra")
animals.remove("badger")
print animals

my_list = [1,9,3,8,5,7]
my_list.sort() #werkt ook voor strings

for number in my_list:
	print number


"""
print("new")

a = 1
b = 2
c = [1, 3, 4]

for item in c:
    print(item)"""

var = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print var['Sloth']
var['Aap']=107
print var
del var['Puffin']
print var
var['Sloth'] = "999"
print var