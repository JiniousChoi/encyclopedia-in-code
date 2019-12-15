#!/usr/bin/env python
import unittest
import datetime

'''
Accessing to attribute with preceding dunder(ex. __local) is automatically converted, hence inaccessible.
'''

class ClassAttributeTest1(object):
    def __init__(self):
        self._sex = 'male'
        self.__age = 18
        self.___addr = 'Seoul'

    def getaddr(self):
        return self.___addr

### Testing part1
cat1 = ClassAttributeTest1()
cat1.getaddr()
cat1._sex
try:
    cat1.__age
    cat1.___addr
except AttributeError:
    #AttributeError: 'ClassAttributeTest1' object has no attribute '__age'
    print('__age & ___addr cannot be accessed from outside')


class ClassAttributeTest2(object):
    def __init__(self):
        self._sex = 'male'
        object.__setattr__(self, 'sex', 'MALE')

#testing
cat2 = ClassAttributeTest2()
assert cat2._sex == 'male'
assert cat2.sex == 'MALE'


class ClassAttributeTest3(object):
    def __init__(self):
        self._sex = 'male'
        #override?
        object.__setattr__(self, '_sex', 'MALE')

    def getsex(self):
        return self._sex

#testing
cat3 = ClassAttributeTest3()
assert cat3._sex == 'MALE'
assert cat3._sex != 'male'
assert cat3.getsex() == 'MALE'


class ClassAttributeTest4(object):
    def __init__(self):
        object.__setattr__(self, 'addr', 'THAI')
        setattr(self, 'name', 'jinsung')

#testing
cat4 = ClassAttributeTest4()
assert cat4.addr == 'THAI'
assert cat4.name == 'jinsung'


class ClassSlotsTest1(object):
    __slots__ = ['__local']

    def __init__(self, obj):
        object.__setattr__(self, '_ClassSlotsTest1__local', obj)

    def run(self):
        return getattr(self.__local, 'day')

    def get(self):
        return self.__local

#testing
dt = datetime.datetime(2015, 1, 1, 0, 0, 0)
cst = ClassSlotsTest1(dt)

assert cst.run() == 1
assert cst.get() is dt
assert cst._ClassSlotsTest1__local is dt

try:
    cst.__local
except AttributeError:
    print('__local is not accessible')


class ClassSlotsTest2(object):
    __slots__ = ['__local']

    def __init__(self):
        pass

    def run(self):
        return self.__local

#testing
cst2 = ClassSlotsTest2()
try:
    cst2.__local
except AttributeError:
    #AttributeError: 'ClassSlotsTest2' object has no attribute '__local'
    pass
try:
    cst2.run()
except AttributeError:
    #AttributeError: _ClassSlotsTest2__local
    pass


class ClassSlotsTest3(object):
    __slots__ = ['__local']

    def __init__(self):
        object.__setattr__(self, '__local', 'jinsung')

#testing
try:
    cst3 = ClassSlotsTest3()
except AttributeError:
    #AttributeError: 'ClassSlotsTest3' object has no attribute '__local'
    pass
