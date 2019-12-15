#!/usr/bin/env python3

import unittest

class Fence:
    def __init__(self, woods):
        self.__woods = woods
        self.size = len(woods)
        self.__init_db()

    def __init_db(self):
        self.__left_db = self.__init_db_to_left()
        self.__right_db = self.__init_db_to_right()

    def height(self, i):
        if i==-1:
            return 0
        elif i==self.size:
            return 0
        else:
            return self.__woods[i]

    def __init_db_to_left(self):
        db = [-1]
        for i,h in enumerate(self.__woods[1:], 1):
            if self.height(i-1) < h:
                db.append(i-1)
            else:
                idx = i-1
                while self.height(idx) >= h:
                    idx = db[idx]
                db.append(idx)

        return db

    def __init_db_to_right(self):
        db = [None]*(self.size-1) + [self.size]
        for i in range(self.size-2, -1, -1):
            h = self.height(i)
            if h > self.height(i+1):
                db[i] = i+1
            else:
                idx = i+1
                while h <= self.height(idx):
                    idx = db[idx]
                db[i]=(idx)

        return db

    def left(self, i):
        return self.__left_db[i]

    def right(self, i):
        return self.__right_db[i]

    def get_max(self):
        res = 0
        for i,height in enumerate(self.__woods):
            width = self.right(i) - self.left(i) - 1
            area = height * width
            res = max(area, res)

        return res
    

class FenceTest(unittest.TestCase):
    def test_db_left(self):
        f = Fence([3,2,1])
        self.assertEqual([f.left(i) for i in [0,1,2]], [-1, -1, -1])

        f = Fence([1,2,3])
        self.assertEqual([f.left(i) for i in [0,1,2]], [-1, 0, 1])

        f = Fence([1,3,2])
        self.assertEqual([f.left(i) for i in [0,1,2]], [-1, 0, 0])

    def test_db_right(self):

        f = Fence([3,2,1])
        self.assertEqual([f.right(i) for i in [2,1,0]], [3,2,1])

        f = Fence([1,2,3])
        self.assertEqual([f.right(i) for i in [2,1,0]], [3, 3, 3])

        f = Fence([1,3,2])
        self.assertEqual([f.right(i) for i in [2,1,0]], [3, 2, 3])

    def assertFence(self, woods, maxsum):
        f = Fence(woods)
        self.assertEqual(f.get_max(), maxsum)

    def test_samples(self):
        self.assertFence(woods=[7,1,5,9,6,7,3], maxsum=20) 
        self.assertFence(woods=[1,4,4,4,4,1,1], maxsum=16) 
        self.assertFence(woods=[1,8,2,2], maxsum=8)

    def test_if_this_takes_O_of_n(self):
        from time import time
        for x in [10000, 50000, 250000]:
            woods = self.generate_woods(x)
            start = time()
            Fence(woods).get_max()
            execution_time = time() - start
            print(x, ':', execution_time)
            ''' YES! it's O(n) as I expected!
            10000 : 0.02214670181274414
            50000 : 0.0985422134399414
            250000 : 0.49942612648010254
            '''

    def generate_woods(self, x):
        ''' return x-length of a list of natural numbers [1,10000]'''
        from random import randint
        return [randint(1,10000) for _ in range(x)]


if __name__=="__main__":
    unittest.main()
