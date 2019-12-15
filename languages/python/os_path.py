#!/usr/bin/python3

from os.path import abspath, basename, dirname, join

print("dirname(__file__) :", dirname(__file__))
print("basename(__file__) :", basename(__file__))
print("dirname(__file__) + basename(__file__): ", dirname(__file__) + basename(__file__)) 
assert dirname(__file__) + basename(__file__) == __file__
print("")

print("__file__: ", __file__)
print("abspath(__file__): ", abspath(__file__))
print("dirname(__file__): ", dirname(__file__))
print("join(dirname(__file__), 'dictionaries'): ", join(dirname(__file__), 'dictionaries'))
print("abspath(join(dirname(__file__), 'dictionaries')) :", abspath(join(dirname(__file__), 'dictionaries')))
print("abspath('jinsung'): ", abspath('jinsung'))
print("dirname(abspath(__file__)): ", dirname(abspath('__file__')))
print("")
