#!/usr/bin/env python3

import unittest

def recurrence(i):
    print(i)
    a = list(range(10000,20000))
    recurrence(i+1)

class RecurrenceErrorTest(unittest.TestCase):
    def test_method1(self):
        try:
            recurrence(1)
            assert False, "cannot reach here"
        except RecursionError as re:
            pass

if __name__=="__main__":
    unittest.main()
